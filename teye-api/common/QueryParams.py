import json
import logging

logger = logging.getLogger("QueryParams")


class QueryParams(dict):
    def __init__(self, request_param: dict, request_body: dict = None):
        self.request_param = request_param
        self.request_body = request_body

        logger.info("Query params: " + json.dumps(request_param, ensure_ascii=False))
        if self.request_body:
            logger.info("Query body: " + json.dumps(request_body, ensure_ascii=False))

    def get_request_body(self):
        return self.request_body

    def get_request_param(self):
        return self.request_param

    def check(self):
        print("check")
