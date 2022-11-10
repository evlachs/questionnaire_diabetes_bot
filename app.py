import ssl
from aiohttp import web

import asyncio

from aiohttp import web
from aiogram import executor, types


from loader import dp
from utils import set_default_commands
from conf import WEBHOOK_URL_PATH, WEBHOOK_URL_BASE, WEBHOOK_SSL_CERT, WEBHOOK_PORT, WEBHOOK_LISTEN, WEBHOOK_SSL_PRIVATE

import handlers

app = web.Application()


async def on_startup():
    await dp.bot.delete_webhook()
    print("EFFO")
    await dp.bot.set_webhook(
        url=f'{WEBHOOK_URL_BASE}{WEBHOOK_URL_PATH}',
        certificate=open(WEBHOOK_SSL_CERT, 'r'),
        drop_pending_updates=True
    )


async def handle(request):
    if request.match_info.get('token') == dp.bot.token:
        request_body_dict = await request.json()
        update = types.Update.as_json(request_body_dict)
        dp.bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)
app.router.add_post('/{token}/', handle)


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIVATE)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(on_startup())
    web.run_app(
        app,
        host=WEBHOOK_LISTEN,
        port=WEBHOOK_PORT,
        ssl_context=context,
    )
