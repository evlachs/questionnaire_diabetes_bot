import asyncio

from aiogram import executor

from web_server import app, setup_app
from loader import dp, context
from conf import WEBHOOK_URL_PATH, WEBHOOK_URL_BASE, WEBHOOK_SSL_CERT, WEBHOOK_PORT, WEBHOOK_LISTEN

import handlers


async def on_startup():
    await dp.bot.delete_webhook()
    print("EFFO")
    await dp.bot.set_webhook(
        url=f'{WEBHOOK_URL_BASE}{WEBHOOK_URL_PATH}',
        certificate=open(WEBHOOK_SSL_CERT, 'r'),
        drop_pending_updates=True
    )


loop = asyncio.new_event_loop()
loop.create_task(on_startup())

if __name__ == '__main__':
    setup_app(app)
    executor.web.run_app(
        app,
        host=WEBHOOK_LISTEN,
        port=WEBHOOK_PORT,
        ssl_context=context,
        loop=loop
    )
