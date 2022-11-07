from aiogram import types
from aiogram.dispatcher import FSMContext

from states import Form
from loader import dp, gc
from messages import MESSAGES
from conf import SPREADSHEET_ID
from spreadsheet_manage import SheetManager


@dp.callback_query_handler(lambda c: c.data in ['gen_test', 'consultation', 'menu'], state=Form.gift)
async def create_and_load_info(callback_query: types.CallbackQuery, state: FSMContext):
    sm = SheetManager(gc, SPREADSHEET_ID)
    async with state.proxy() as data:
        if callback_query.data == 'gen_test':
            data['gift'] = 'Первичная расшифровка генетического теста'
            await dp.bot.send_message(callback_query.from_user.id, MESSAGES['share_contact'])
            await Form.contact.set()
        elif callback_query.data == 'consultation':
            data['gift'] = 'Консультация с доктором'
            await dp.bot.send_message(callback_query.from_user.id, MESSAGES['share_contact'])
            await Form.contact.set()
        elif callback_query.data == 'menu':
            data['gift'] = 'Примеры меню питания'
            data['contact'] = None
            await dp.bot.send_message(callback_query.from_user.id, MESSAGES['menu_gift'])
            empty_cell_index = sm.get_empty_cell_index()
            sm.load_new_user_info(data, empty_cell_index)
            sm.add_quest_passed_value()
            await state.finish()
