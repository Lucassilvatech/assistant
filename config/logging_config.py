import logging
import logging.config

class LoggingConfig:

    @staticmethod    
    def setup_logging():
        logging.config.dictConfig({
            "version": 1,
            "disable_existing_loggers": False,

            "formatters": {
                "default": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                },
            },

            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "level": "INFO",
                },
                "file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": "logs/app.log",
                    "maxBytes": 1_000_000,
                    "backupCount": 3,
                    "formatter": "default",
                    "level": "DEBUG",
                    "encoding": "utf-8"
                },
            },

            "root": {
                "handlers": ["file"],
                "level": "DEBUG",
            }
        })