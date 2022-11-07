from aiogram import executor

from loader import dp
from utils import set_default_commands

import handlers


async def on_startup(dispatcher):
    """Sets default commands for the bot, initializes the client, launches the loop with the invite_users function"""
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
