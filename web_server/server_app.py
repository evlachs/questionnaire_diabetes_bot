import jinja2
import aiohttp_jinja2

from aiohttp import web
from aiogram import types

from web_app import setup_routes as setup_forum_routes

from loader import dp


def setup_routes(application):
    setup_forum_routes(application)


def setup_external_libraries(application: web.Application) -> None:
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))


def setup_app(application):
    setup_external_libraries(application)
    setup_routes(application)


async def handle(request):
    print(request, '\n', request.match_info.get('token'))
    if request.match_info.get('token') == dp.bot.token:
        print('HGASGKGKASJGDJKHGASJKHGDKJHGA')
        request_body_dict = await request.json()
        update = types.Update.as_json(request_body_dict)
        dp.bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)


app = web.Application()

app.router.add_post('/{token}/', handler=handle)
