import settings
from watcher import Watcher
from notifier import Notifier
from settings import rules

filepath = settings.filepath
time_to_check_updates = settings.rescan_interval
time_to_notify_user = settings.notify_interval
messages = []

watcher = Watcher(filepath, messages, time_to_check_updates, rules)
notifier = Notifier(time_to_notify_user, messages)
