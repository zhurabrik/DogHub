import os
import logging

from aiohttp import web
from configargparse import Namespace
from functools import partial
from sqlalchemy.ext.asyncio import create_async_engine

from backend.handlers import routes
from backend.config import parse_args
from backend.middlewares.error_middleware import error_middleware
from backend.middlewares.logging_middleware import logging_middleware


log_filename = os.path.join(os.path.dirname(__file__), "debug.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s:%(message)s",
    handlers=[
        logging.FileHandler(log_filename, mode="w"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


async def db_engine(app: web.Application, args: Namespace):
    app["db_engine"] = create_async_engine(
        args.db_url, echo=args.log_sql, hide_parameters=False
    )

    yield
    await app["db_engine"].dispose()


def create_app(args: Namespace) -> web.Application:
    app = web.Application(middlewares=[logging_middleware, error_middleware])
    app.add_routes(routes)
    app.cleanup_ctx.append(partial(db_engine, args=args))
    return app


def main():
    args = parse_args()
    app = create_app(args)

    web.run_app(
        app,
        port=args.port,
    )


if __name__ == "__main__":
    main()
