from web_server.web_app.forum import views
from aiohttp import web
from loader import dp
from aiogram import types
from conf import BOT_TOKEN


async def handle(request):
    if request.match_info.get_info()['path'].strip('/') == BOT_TOKEN:
        request_body_dict = await request.json()
        print(request.match_info.get_info())
        print(request_body_dict)
        update = types.Update.to_object(request.match_info.get_info())
        print(type(update), update)
        await dp.process_update(update)
        return web.Response()
    else:
        return web.Response(status=403)


def setup_routes(app):
    app.router.add_get('/', views.index)
    app.router.add_post(f'/{BOT_TOKEN}', handler=handle)
