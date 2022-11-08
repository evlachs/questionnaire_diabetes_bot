from aiogram import executor

from loader import dp
from utils import set_default_commands
from conf import WEBHOOK_URL_PATH, WEBHOOK_URL_BASE, WEBHOOK_SSL_CERT, WEBHOOK_PORT, WEBHOOK_LISTEN

import handlers


async def on_startup(dispatcher):
    """Sets default commands for the bot, initializes the client, launches the loop with the invite_users function"""
    await set_default_commands(dispatcher)
    await dp.bot.delete_webhook()
    await dp.bot.set_webhook(
        url=f'{WEBHOOK_URL_BASE}{WEBHOOK_URL_PATH}',
        certificate=open(WEBHOOK_SSL_CERT, 'r'),
        drop_pending_updates=True
    )


if __name__ == '__main__':
    executor.start_webhook(
        dp,
        webhook_path=WEBHOOK_URL_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBHOOK_LISTEN,
        port=WEBHOOK_PORT
    )
