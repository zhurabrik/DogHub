from aiohttp import web

routes = web.RouteTableDef()

from backend.handlers.ping import ping
from backend.handlers.templates import get_template, get_templates
