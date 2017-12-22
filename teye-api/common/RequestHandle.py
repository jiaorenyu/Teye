# -*- coding: utf-8 -*-

import logging
import sys

import tornado.web

from common.QueryParams import QueryParams
from common.Response import Response
from common.ResponseStatusCode import ResponseStatusCode
from exception.BadRequest import BadRequest
from exception.Unauthorized import Unauthorized

logger = logging.getLogger("RequestHandle")


def request_handle(request_handler: tornado.web.RequestHandler, query_params: QueryParams):
    response = Response()
    result = dict()
    try:
        print("")
        query_params.check()
    except BadRequest as e:
        msg = str(e)
        logger.warn(msg)
        code = ResponseStatusCode.BAD_REQUEST.value
        response.__init__(resp_status=code,
                          code=code,
                          msg=msg,
                          result=result)
    except Unauthorized as e:
        msg = str(e)
        logger.warn(msg)
        code = ResponseStatusCode.UNAUTHORIZED.value
        response.__init__(resp_status=code,
                          code=code,
                          msg=msg,
                          result=result)

    except Exception as e:
        print(str(e))
        print(sys.exc_info()[0])
        msg = str(e)
        logger.warn(msg)
        code = ResponseStatusCode.INTERNAL_SERVER_ERROR.value
        response.__init__(resp_status=code,
                          code=code,
                          msg=msg,
                          result=result)
    else:
        code = ResponseStatusCode.SUCCESS.value
        response.__init__(resp_status=code,
                          code=code,
                          msg="OK",
                          result=result)

    response_str = response.generate_response(request_handler)
    return response_str
