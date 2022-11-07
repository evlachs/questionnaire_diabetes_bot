from aiogram import types
from conf import BOT_URL


go_to_quest_button = types.InlineKeyboardButton('Заполнить анкету', url=BOT_URL)

go_to_quest_keyboard = types.InlineKeyboardMarkup()
go_to_quest_keyboard.add(go_to_quest_button)
