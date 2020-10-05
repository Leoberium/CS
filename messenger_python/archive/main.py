import time
from collections import namedtuple


class Messenger:
    message_template = namedtuple("Message",
                                  ("text", "author", "time"))

    def __init__(self):
        self.db = []

    def send_message(self, text, author):
        if isinstance(text, str) and isinstance(author, str):
            self.db.append(self.message_template(text, author, time))
            return True
        else:
            return False

    def get_messages(self):
        return self.db


if __name__ == '__main__':
    pass
