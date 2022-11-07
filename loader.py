import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import gspread

from conf import BOT_TOKEN, SERVICE_ACCOUNT

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

gc = gspread.service_account(SERVICE_ACCOUNT)
