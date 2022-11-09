import cherrypy

from aiogram import executor

from cherry import WebhookServer

from loader import dp
from utils import set_default_commands
from conf import WEBHOOK_URL_PATH, WEBHOOK_URL_BASE, WEBHOOK_SSL_CERT, WEBHOOK_PORT, WEBHOOK_LISTEN, WEBHOOK_SSL_PRIVATE

import handlers


# async def on_startup(dispatcher):
#     """Sets default commands for the bot, initializes the client, launches the loop with the invite_users function"""
# set_default_commands(dp)
dp.bot.delete_webhook()
dp.bot.set_webhook(
    url=f'{WEBHOOK_URL_BASE}{WEBHOOK_URL_PATH}',
    certificate=open(WEBHOOK_SSL_CERT, 'r'),
    drop_pending_updates=True
)

cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIVATE
})


if __name__ == '__main__':
    # executor.start_polling(
    #     dp,
    #     on_startup=on_startup,
    # )
    cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})
