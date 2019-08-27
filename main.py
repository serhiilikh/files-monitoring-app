from watcher import Watcher
from notifier import Notifier
from settings import rules, rescan_interval, notify_interval, filepath

messages = []

watcher = Watcher(filepath, messages, rescan_interval, rules)
notifier = Notifier(notify_interval, messages)
