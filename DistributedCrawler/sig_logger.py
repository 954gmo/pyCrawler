# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import logging
from logging import config
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INFO_LOG = os.path.join(BASE_DIR, 'log', 'info.log')
ERR_LOG = os.path.join(BASE_DIR, 'log', 'error.log')

if not os.path.exists(INFO_LOG):
    os.makedirs(INFO_LOG, mode=0o777)

if not os.path.exists(ERR_LOG):
    os.makedirs(ERR_LOG, mode=0o777)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    # "root": {
    #     "level": "INFO",
    #     "handlers": ["info"]
    # }, # will make INFO duplicated.
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "info": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": INFO_LOG,
            "formatter": "info",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": ERR_LOG,
            "formatter": "error",
        },
        "debug": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "debug"
        }
    },
    "loggers": {
        "console": {
            "handlers": ['console'],
            "level": "INFO",
            "propagate": False,
        },
        "debug": {
            "handlers": ['debug'],
            "level": "DEBUG",
            "propagate": False,
        },
        "info": {
            "handlers": ["info"],
            "level": "INFO",
            "propagate": True
        },
        "error": {
            "handlers": ["error"],
            "level": "ERROR",
            "propagate": True
        },
    },
    "formatters": {
        "error": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },

        "info": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "debug": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "console": {
            "format": (
                u"%(asctime)s "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",

        }
    },
}

config.dictConfig(LOGGING)
info_logger = logging.getLogger("info")
err_logger = logging.getLogger("error")
debug_logger = logging.getLogger("debug")
console = logging.getLogger("console")


def console_info(msg):
    info_logger.info(msg)
    console.info(msg)


def console_err(msg):
    err_logger.info(msg)
    console.info(msg)
