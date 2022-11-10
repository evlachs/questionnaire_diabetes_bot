from web_server.web_app.forum import views
from aiohttp import web
from loader import dp
from aiogram import types
from conf import BOT_TOKEN


async def handle(request):
    print(request, '\n', request.match_info.get_info().path)
    if request.match_info.get_info()['path'].strip('/') == BOT_TOKEN:
        print('HGASGKGKASJGDJKHGASJKHGDKJHGA')
        request_body_dict = await request.json()
        update = types.Update(request_body_dict)
        dp.bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)


def setup_routes(app):
    app.router.add_get("/", views.index)
    app.router.add_post(f'/{BOT_TOKEN}', handler=handle)
