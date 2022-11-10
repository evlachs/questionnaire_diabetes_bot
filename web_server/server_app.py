import jinja2
import aiohttp_jinja2

from aiohttp import web

from web_server.web_app import setup_routes as setup_forum_routes


def setup_routes(application):
    setup_forum_routes(application)


def setup_external_libraries(application: web.Application) -> None:
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))


def setup_app(application):
    setup_external_libraries(application)
    setup_routes(application)


app = web.Application()
