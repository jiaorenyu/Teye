import fcntl
import logging
import os

logger = logging.getLogger("file_util")


def fcntl_lock(lock):
    def dec(func):
        def new_func(*arg, **kws):
            fp = open(lock, "w")
            try:
                fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except IOError as e:
                logger.warning("{0} is already running.\nmessage: ".format(func, e))
                exit(1)
            func(*arg, **kws)

        return new_func

    return dec


def get_set(fn):
    ids = set()
    fp = open(fn, "r")
    for line in fp:
        line.strip()
        ids.add(line)
    fp.close()

    return ids


def ensure_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        if os.path.isfile(path):
            logger.error("{} is not a folder!")
            exit(2)
