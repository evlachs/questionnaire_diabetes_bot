from aiogram.types import BotCommand


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand('cancel', 'отменить действие'),
            BotCommand('start', 'пройти анкету')
        ]
    )
