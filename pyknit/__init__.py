# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later
import logging

from .GaugeSwatch import *
from .Chart import *
from .Hat import *

logging_config_dict = dict(
    version=1,
    formatters={
        "simple": {
            "format": """%(asctime)s | %(name)-12s | %(levelname)-8s | %(message)s"""
        }
    },
    handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    root={"handlers": ["console"], "level": logging.DEBUG},
)

from .pyknitter import *
