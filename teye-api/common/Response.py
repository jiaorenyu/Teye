import json


class Response:
    def __init__(self, resp_status=200, code=0, msg="OK", result={},
                 suppress_response_codes=False, callback=None):
        self.resp_status = resp_status
        self.code = code
        self.msg = msg
        self.result = result
        self.suppress_response_codes = suppress_response_codes
        self.callback = callback

    def set_suppress_response_codes(self, suppress_response_codes):
        self.suppress_response_codes = suppress_response_codes

    def set_callback(self, callback):
        self.callback = callback

    def to_dict(self):
        response = dict()
        response["code"] = self.code
        response["msg"] = self.msg
        if self.code == 0:
            response["data"] = self.result

        return response

    def generate_response(self, request_handler):

        response_dict = self.to_dict()
        response_str = json.dumps(response_dict, ensure_ascii=False)

        request_handler.set_header("Content-Type", "application/json;charset=utf-8")

        request_handler.set_status(self.resp_status)
        if self.suppress_response_codes:
            request_handler.set_status(200)

        if self.callback:
            request_handler.set_header("Content-Type", "application/javascript;charset=utf-8")
            request_handler.set_status(200)
            response_str = self.callback + "(" + response_str + ")"

        return response_str
