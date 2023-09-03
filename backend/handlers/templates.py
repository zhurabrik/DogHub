import logging
import json

import json

from aiohttp import web
import sqlalchemy as sa

from backend.handlers import routes
from backend.utils.decorators import decorator_logging_factory_async
import backend.db.schema as db


logger = logging.getLogger(__name__)


def format_template(template: list) -> str:
    return json.dumps({"id": template[0], **template[1]})


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
        body=format_template(template),
        status=web.HTTPOk.status_code,
    )


@routes.post("/template")
@decorator_logging_factory_async(logger)
async def post_template(request: web.Request):
    data = await request.json()
    logger.info(data)
    async with request.app["db_engine"].begin() as db_conn:
        new_template = await db_conn.execute(
            sa.insert(db.templates_table).values(meta=data)
        )
        await db_conn.commit()
    return web.json_response(
        body=f'{{"id": {new_template.inserted_primary_key[0]}}}',
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

    formatted_templates = (
        f'[{",".join([format_template(template) for template in templates])}]'
    )

    return web.json_response(
        body=f'{{"templates": {formatted_templates}}}',
        status=web.HTTPOk.status_code,
    )
