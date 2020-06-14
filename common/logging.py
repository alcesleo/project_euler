"""Configures the standard logging library
"""

import os
import logging

LOG_LEVEL = os.environ.get("LOG_LEVEL", "WARNING").upper()
FORMAT = "%(message)s"

logging.basicConfig(level=LOG_LEVEL, format=FORMAT)

logger = logging.getLogger()
debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
