import logging

import gspread

import ssl

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from conf import BOT_TOKEN, SERVICE_ACCOUNT, WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIVATE

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

gc = gspread.service_account(SERVICE_ACCOUNT)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIVATE)
