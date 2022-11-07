from aiogram import types
from aiogram.dispatcher import FSMContext

from states import Form
from messages import MESSAGES
from loader import dp, bot, gc
from conf import SPREADSHEET_ID
from keyboards import choose_gift_keyboard
from spreadsheet_manage import SheetManager


@dp.message_handler(commands=['start'])
async def start_message_processing(message: types.Message, state: FSMContext):
    sm = SheetManager(gc, SPREADSHEET_ID)
    if sm.check_user_in_spreadsheet(str(message.from_user.id)):
        await bot.send_message(message.from_user.id, MESSAGES['already_passed'])
        return
    sm.add_bot_activates_value()
    async with state.proxy() as data:
        data['user_id'] = message.from_user.id
        data['user_firstname'] = message.from_user.first_name
        data['user_lastname'] = message.from_user.last_name
        data['username'] = '@' + message.from_user.username
    await bot.send_message(message.chat.id, MESSAGES['set_name'])
    await Form.name.set()


@dp.message_handler(state=Form.name)
async def set_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await bot.send_message(message.chat.id, MESSAGES['who_has_diabetes'])
    await Form.sick_person.set()


@dp.message_handler(state=Form.sick_person)
async def set_sick_person(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sick_person'] = message.text
    await bot.send_message(message.chat.id, MESSAGES['set_diabetes_type'])
    await Form.diabetes_type.set()


@dp.message_handler(state=Form.diabetes_type)
async def set_sick_person(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['diabetes_type'] = message.text
    await bot.send_message(message.chat.id, MESSAGES['how_long'])
    await Form.how_long.set()


@dp.message_handler(state=Form.how_long)
async def set_sick_person(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['how_long'] = message.text
    await bot.send_message(message.chat.id, MESSAGES['set_medium_sugars'])
    await Form.medium_sugars.set()


@dp.message_handler(state=Form.medium_sugars)
async def set_sick_person(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['medium_sugars'] = message.text
    await bot.send_message(message.chat.id, MESSAGES['how_much_insulin'])
    await Form.how_much_insulin.set()


@dp.message_handler(state=Form.how_much_insulin)
async def set_sick_person(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['how_much_insulin'] = message.text
    await bot.send_message(message.chat.id, MESSAGES['what_help'])
    await Form.help.set()


@dp.message_handler(state=Form.help)
async def set_sick_person(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['help'] = message.text
    await bot.send_message(message.chat.id, MESSAGES['what_result'])
    await Form.result.set()


@dp.message_handler(state=Form.result)
async def set_sick_person(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['result'] = message.text
    await bot.send_message(message.chat.id, MESSAGES['set_gift'], reply_markup=choose_gift_keyboard)
    await Form.gift.set()


@dp.message_handler(state=Form.contact)
async def set_sick_person(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, MESSAGES['thanks_for_passing'])
    sm = SheetManager(gc, SPREADSHEET_ID)
    async with state.proxy() as data:
        data['contact'] = message.text
        empty_cell_index = sm.get_empty_cell_index()
        sm.load_new_user_info(data, empty_cell_index)
        sm.add_quest_passed_value()
        await state.finish()
