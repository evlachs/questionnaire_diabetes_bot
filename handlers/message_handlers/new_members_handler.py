import asyncio

from aiogram import types

from messages import MESSAGES
from loader import dp, bot, gc
from conf import SPREADSHEET_ID
from keyboards import go_to_quest_keyboard
from spreadsheet_manage import SheetManager


async def delete_message(message: types.Message, time: int):
    await asyncio.sleep(time)
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(content_types=['new_chat_members', 'left_chat_member'])
async def del_welcome_message(message: types.Message):
    print(message)
    sm = SheetManager(gc, SPREADSHEET_ID)
    if message.content_type == 'new_chat_members':
        sm.add_new_member()
        msg = await bot.send_message(
            message.chat.id,
            MESSAGES['welcome_message'],
            reply_markup=go_to_quest_keyboard,
        )
        await delete_message(msg, 30)
    elif message.content_type == 'left_chat_member':
        sm.add_left_member()
