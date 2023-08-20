import json
import logging
from typing import Callable

from aiohttp import web

logger = logging.getLogger(__name__)


def error_response(error_message: str, status_code: int):
    return web.json_response(data={"error": error_message}, status=status_code)


@web.middleware
async def error_middleware(request: web.Request, handler: Callable):
    try:
        return await handler(request)
    except web.HTTPException as err:
        return error_response(err.text or str(err), err.status_code)
    except json.JSONDecodeError:
        return error_response(
            "json body required", web.HTTPBadRequest.status_code
        )
    except Exception as err:
        logger.exception(err)
        return error_response(
            "unexpected error", web.HTTPInternalServerError.status_code
        )
