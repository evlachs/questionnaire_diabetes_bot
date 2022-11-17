import string
import asyncio
import json

from aiogram import types

from messages import MESSAGES
from loader import dp, bot, gc
from conf import SPREADSHEET_ID, GROUP_ID
from spreadsheet_manage import SheetManager


async def delete_message(message: types.Message, time: int):
    await asyncio.sleep(time)
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(content_types=['text', 'photo'])
async def filter_messages(message: types.Message):
    current_chat_id = message.chat.id
    if current_chat_id != GROUP_ID:
        return
    sm = SheetManager(gc, SPREADSHEET_ID)
    sm.add_new_message()
    # message_content = set()
    # bad_words_content = set(json.load(open('data/bad_words.json')))
    # if message.content_type == 'photo':
    #     text = message.caption
    # else:
    #     text = message.text
    # if not text:
    #     return
    # for word in text.split():
    #     translated_word = word.lower().translate(str.maketrans('', '', string.punctuation))
    #     message_content.add(translated_word)
    # if message_content.intersection(bad_words_content):
    #     msg = await message.reply(MESSAGES['filter'])
    #     await message.delete()
    #     await delete_message(msg, 3)
