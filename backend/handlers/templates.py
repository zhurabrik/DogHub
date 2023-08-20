import logging
import json

from aiohttp import web
import sqlalchemy as sa

from backend.handlers import routes
from backend.utils.decorators import decorator_logging_factory_async
import backend.db.schema as db


logger = logging.getLogger(__name__)


def format_template(template: list) -> dict[str, dict]:
    return {"template_id": template[0], "meta": template[1]}


@routes.get("/template")
@decorator_logging_factory_async(logger)
async def get_template(request: web.Request):
    async with request.app["db_engine"].begin() as db_conn:
        template = (
            await db_conn.execute(
                sa.select(
                    db.templates_table.c.id, db.templates_table.c.meta
                ).where(
                    db.templates_table.c.id
                    == int(request.query.get("template_id"))
                )
            )
        ).fetchone()

    if template is None:
        raise web.HTTPNotFound(text="template not found")

    return web.Response(
        body=f"{format_template(template)}",
        content_type="application/json",
        status=web.HTTPOk.status_code,
    )


@routes.get("/templates")
@decorator_logging_factory_async(logger)
async def get_templates(request: web.Request):
    async with request.app["db_engine"].begin() as db_conn:
        templates = (
            await db_conn.execute(
                sa.select(db.templates_table.c.id, db.templates_table.c.meta)
                .limit(request.query.get("limit"))
                .offset(request.query.get("offset"))
            )
        ).fetchall()

    formatted_templates = [format_template(template) for template in templates]

    return web.Response(
        body=f'{{"templates": {formatted_templates}}}',
        content_type="application/json",
        status=web.HTTPOk.status_code,
    )
