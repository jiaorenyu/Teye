import logging
import os
import sys

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from handler.MainHandler import EchoHandler

from util import token_auth
from util.file_util import fcntl_lock, ensure_dir
from util.log_util import logging_config

define("port", default=8000, help="run on the given port", type=int)
define("configfile", default="server.conf", help="run on the given port", type=str)
define("pidfile", type=str)

define("access_log", default=None, type=str)
define("debug_log", default=None, type=str)
define("info_log", default=None, type=str)
define("warn_log", default=None, type=str)
define("err_log", default=None, type=str)

define("log_level", default=None, type=str)

define("tokens", default=None, type=str)

logger = logging.getLogger("main")


@fcntl_lock("/tmp/teye-api.lock")
def main():
    # Parse options
    tornado.options.parse_command_line()
    if len(sys.argv) > 1 and sys.argv[1] == "help":
        options.print_help()
        exit()
    tornado.options.parse_config_file(options.configfile)

    # Configure logging
    # We cannot use logging.basicConfig because tornado has
    # set up loggers when parsing options
    logging_config(
        options.access_log,
        options.debug_log,
        options.info_log,
        options.warn_log,
        options.err_log,
        options.log_level
    )

    tokens = options.tokens.split(",")
    token_auth.init(tokens)

    # Set up application
    app = tornado.web.Application(handlers=[
        (r"/", EchoHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    pidfile = options.pidfile
    ensure_dir(os.path.dirname(pidfile))
    pidfp = open(pidfile, "w")
    pidfp.write(str(os.getpid()))
    pidfp.close()

    logger.info("Starting tornado server on port {}...".format(options.port))

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
