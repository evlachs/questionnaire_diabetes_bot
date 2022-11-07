from aiogram import types


menu_gift_button = types.InlineKeyboardButton('меню', callback_data='menu')
gen_test_button = types.InlineKeyboardButton('первичная расшифровка', callback_data='gen_test')
consultation_button = types.InlineKeyboardButton('консультация', callback_data='consultation')

choose_gift_keyboard = types.InlineKeyboardMarkup()
choose_gift_keyboard.add(menu_gift_button).add(gen_test_button).add(consultation_button)
