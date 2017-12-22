import logging
import time

format_list = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]

logger = logging.getLogger("time_util")


def get_second(timestr, format="%Y-%m-%d"):
    return int(time.mktime(time.strptime(timestr, format)))
