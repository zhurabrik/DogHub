import logging
from time import monotonic
from typing import Callable

from aiohttp import web

logger = logging.getLogger(__name__)


@web.middleware
async def logging_middleware(request: web.Request, handler: Callable):
    time_start = monotonic()
    response: web.Response = await handler(request)
    time_end = monotonic()
    time_execution = round((time_end - time_start) * 1000, 2)

    log_message = f"{request.method} {request.path} {response.status} " f"{time_execution}ms"
    if response.status < 500:
        logger.info(log_message)
    else:
        logger.error(log_message)

    return response
