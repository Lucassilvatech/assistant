import logging


class Logger:
 
    @staticmethod
    def get_logger(name: str):
        return logging.getLogger(name)
