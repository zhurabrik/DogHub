import logging
from aiohttp import web
import sqlalchemy as sa

from backend.utils.decorators import decorator_logging_factory_async
from backend.handlers import routes

logger = logging.getLogger(__name__)


@routes.get("/ping")
@decorator_logging_factory_async(logger)
async def ping(request: web.Request):
    return web.json_response(
        data={"message": "ok"}, status=web.HTTPOk.status_code
    )


@routes.get("/ping_db")
@decorator_logging_factory_async(logger)
async def ping_db(request: web.Request):
    async with request.app["db_engine"].begin() as db_conn:
        await db_conn.execute(sa.text("SELECT 1;"))
    return web.HTTPOk(
        text='{"message": "connected"}',
        headers={"content-type": "application/json"},
    )
