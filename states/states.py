from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    sick_person = State()
    diabetes_type = State()
    how_long = State()
    medium_sugars = State()
    how_much_insulin = State()
    help = State()
    result = State()
    gift = State()
    contact = State()
