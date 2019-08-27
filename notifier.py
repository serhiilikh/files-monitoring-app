from time import sleep
import logging


class Notifier:
    def _notify_user(self):
        if self.messages_to_send:
            print(self.messages_to_send)
            self.messages_to_send = []

    def __init__(self, time_to_notify, messages):
        self.messages = messages
        self.messages_to_send = []
        while True:
            self.messages_to_send, self.messages = self.messages, self.messages_to_send
            self._notify_user()
            sleep(time_to_notify)
