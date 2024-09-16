import logging.config

from .config import FLASK_ENV


DEV_LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

PROD_LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
        },
        # "file": {
        #     "class": "logging.FileHandler",
        #     "filename": "errors.log",
        #     "level": "ERROR",
        #     "formatter": "standard",
        # },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

if FLASK_ENV == "development":
    logging.config.dictConfig(DEV_LOGGING_CONFIG)
else:
    logging.config.dictConfig(PROD_LOGGING_CONFIG)
