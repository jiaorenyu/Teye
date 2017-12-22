import logging
import os
from logging.handlers import TimedRotatingFileHandler

from util.file_util import ensure_dir

FORMAT = "[%(asctime)s %(name)s %(levelname)s] %(message)s"
DATEFMT = '%Y-%m-%d %I:%M:%S'

formatter = logging.Formatter(FORMAT, DATEFMT)

logLevel = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARN,
    "error": logging.ERROR
}


def logging_config(
        access_log=None,
        debug_log=None,
        info_log=None,
        warn_log=None,
        err_log=None,
        log_level=None
):
    if access_log is not None:
        ensure_dir(os.path.dirname(access_log))
        h = TimedRotatingFileHandler(access_log, "D")
        h.setLevel(logging.INFO)
        h.setFormatter(formatter)
        logging.getLogger("tornado.access").addHandler(h)

    handlers = []

    def add_handler(filename, level):
        ensure_dir(os.path.dirname(filename))
        h = TimedRotatingFileHandler(filename, "D", encoding="utf8")
        h.setLevel(level)
        h.setFormatter(formatter)
        handlers.append(h)

    if debug_log is not None:
        add_handler(debug_log, logging.DEBUG)
    if info_log is not None:
        add_handler(info_log, logging.INFO)
    if warn_log is not None:
        add_handler(warn_log, logging.WARN)
    if err_log is not None:
        add_handler(err_log, logging.ERROR)

    root_logger = logging.root
    root_logger.setLevel(logLevel[log_level])
    for h in handlers:
        root_logger.addHandler(h)
