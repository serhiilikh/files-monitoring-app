from threading import Thread
import time
import os
from importlib import import_module


class Watcher(Thread):
    def __init__(self, filepath, messages, time_to_check_updates, rules):
        super(Watcher, self).__init__()
        self.daemon = True
        self.start()
        self.messages = messages
        self.filepath = filepath
        self.tracker = {}
        self.handlers_by_item_type_list = []
        for rule in rules:
            if rule["active"]:
                module = import_module(rule["handler"].replace("/", "."))
                handler = module.Handler()
                item_type = rule["item_type"]
                self.handlers_by_item_type_list.append({"item_type": item_type,
                                                        "handler_instance": handler,
                                                        "parameters": rule})

        scan_succesfull = False
        while not scan_succesfull:
            scan_succesfull = self._do_first_scan()
        while True:
            self._rescan()
            time.sleep(time_to_check_updates)

    def _do_first_scan(self):
        try:
            for r, d, f in os.walk(self.filepath):
                for item in f+d:
                    path = r + "/" + item if not r.endswith("/") else r + item
                    self.tracker[path] = os.path.getmtime(path)
        except OSError:
            return False
        print("initial scan ended. tracking {} items".format(len(self.tracker)))
        return True

    def _rescan(self):
        for r, d, f in os.walk(self.filepath):
            for item in f+d:
                path = r + "/" + item if not r.endswith("/") else r + item
                try:
                    mtime = os.path.getmtime(path)
                    if path not in self.tracker or self.tracker[path] < mtime:
                        print("item added or changed! - {}".format(path))
                        handlers_for_job = []
                        item_type = ""
                        if os.path.isdir(path):
                            item_type = "folder"
                        elif os.path.islink(path):
                            item_type = "link"
                        elif os.path.isfile(path):
                            item_type = "file"
                        for handler in self.handlers_by_item_type_list:
                            if item_type == "file" and path.endswith(handler["item_type"]) \
                                    or item_type == handler["item_type"]:
                                handlers_for_job.append(handler)
                                # handler["handler_instance"].do_job(file, handler)
                        for handler in handlers_for_job:
                            # if one of handlers is "remove" item and path wont exist anymore
                            if item and path:
                                result_info, new_path = handler["handler_instance"].do_job(path, item,
                                                                                           handler["parameters"])
                                # if file is removed entirely
                                if new_path is False and path in self.tracker:
                                    del self.tracker[path]
                                    item, path = None, None
                                elif path != new_path and path in self.tracker:
                                    del self.tracker[path]
                                self.tracker[new_path] = os.path.getmtime(new_path)
                                # this list of messages is also used in notifier
                                self.messages += result_info
                except OSError:
                    continue
