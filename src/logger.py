""" logger.py"""

import sys
import logging
from src.constants import get_config

FORMATTER = logging.Formatter(f"[{get_config('parameters', 'env')}] "
                              f"[%(levelname)s]: [%(asctime)s] [%(lineno)d] [%(filename)s] [%(message)s]")


def get_console_handler():
    """
    Returns
        console_handler
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    console_handler.setLevel(logging.INFO)
    return console_handler


def set_up_logging():
    """
    Returns
        logger
    """
    _logger = logging.getLogger(__name__)
    if not _logger.hasHandlers():
        _logger.setLevel(logging.DEBUG)
        _logger.addHandler(get_console_handler())
        _logger.propagate = False

    return _logger


logger = set_up_logging()
