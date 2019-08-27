from os import rename, mkdir
from os.path import isdir
from .handler_base import HandlerBase


class Handler(HandlerBase):
    def do_job(self, path, item_name, handler_dict):
        path_to_new_folder = handler_dict["value_1"]
        new_path = path_to_new_folder + item_name
        if not isdir(path_to_new_folder):
            mkdir(path_to_new_folder)
        try:
            rename(path, new_path)
        except FileExistsError:
            # in case of file already exists in that folder
            import time
            rename(path, path_to_new_folder + str(int(time.time())) + "-" + item_name)
        return "item {} moved from {} to {}".format(item_name, path, new_path), new_path
