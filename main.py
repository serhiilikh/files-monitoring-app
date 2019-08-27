from watcher import Watcher
from settings import rules, rescan_interval, notify_interval, workdir
from queue import Queue
messages = Queue

watcher = Watcher(workdir, messages, rescan_interval, rules)
