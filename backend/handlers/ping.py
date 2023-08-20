import logging
from aiohttp import web

from backend.utils.decorators import decorator_logging_factory_async
from backend.handlers import routes

logger = logging.getLogger(__name__)


@routes.get("/ping")
@decorator_logging_factory_async(logger)
async def ping(request: web.Request):
    return web.json_response(
        data={"message": "ok"}, status=web.HTTPOk.status_code
    )
