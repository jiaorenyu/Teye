import json
import logging

import tornado.web

from common.RequestHandle import request_handle
from teye_common.TeyeQueryParams import TeyeQueryParams

logger = logging.getLogger("handlers")


class EchoHandler(tornado.web.RequestHandler):

    def get(self):
        request_param = {k: self.request.arguments[k][0].decode("utf-8") for k in
                         self.request.arguments}

        query_params = TeyeQueryParams(request_param)
        resp_str = request_handle(self, query_params)
        self.write(resp_str)
