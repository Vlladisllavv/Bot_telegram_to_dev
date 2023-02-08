from aiogram import types, Dispatcher
from create_bot import dp, bot
from database.database import create_profile
from keyboard import create_keyboard, kb_edit


HELP_COMMAND="""
/start - начать работу
/help - список команд
/currency - клавиатура валют
/update - изменить клавиатуру
"""


#@dp.message_handler(commands=['start'])
async def start_info(message: types.Message):
	await bot.send_message(message.from_user.id, text=f'Привет {message.from_user.full_name}, используй /help')

#@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
	await bot.send_message(message.from_user.id, f'{HELP_COMMAND}')
	await create_profile(user_id=message.from_user.id, full_name=message.from_user.full_name, first_name=message.from_user.first_name, user_name=message.from_user.username)
	print('Нам пишет: ', message.from_user.id, message.from_user.full_name, message.from_user.first_name, message.from_user.username)


#@dp.message_handler(commands=['currency'])
async def currency_cash(message: types.Message):
	await bot.send_message(message.from_user.id, text="Выбери валюту", reply_markup=await create_keyboard(message))
	

#@dp.message_handler(commands=['update'])
async def update_key(message: types.Message):
	await bot.send_message(message.from_user.id, text='Что ты хочешь сделать с кнопками?',
	reply_markup=kb_edit)


def register_main_handlers(dp: Dispatcher):
	dp.register_message_handler(start_info, commands=['start'])
	dp.register_message_handler(help_command, commands=['help'])
	dp.register_message_handler(currency_cash, commands=['currency'])
	dp.register_message_handler(update_key, commands=['update'])





