import readline
import os


class History:
    def __init__(self, history_file=".history"):
        self.history_file = history_file

    def load_history(self):
        if os.path.exists(self.history_file):
            readline.read_history_file(self.history_file)

    def save_history(self):
        readline.write_history_file(self.history_file)
