from  utils.logger import Logger

import readline
import os


class History:
    def __init__(self, history_file=".history"):
        self.history_file = history_file
        self.logger = Logger.get_logger(__name__)

    def load_history(self):
        if os.path.exists(self.history_file):
            readline.read_history_file(self.history_file)
            self.logger.info(f"History loaded from {self.history_file}")

    def save_history(self):
        readline.write_history_file(self.history_file)
        self.logger.info(f"History saved to {self.history_file}")