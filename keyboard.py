from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database.database import check_custom_button_ripple, check_custom_button_tether
from aiogram import types

kb_edit = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_edit.add(KeyboardButton('Добавить валюту'))
kb_edit.add(KeyboardButton('Удалить валюту'))


kb_choise = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_choise.add(KeyboardButton('Добавить Tether'))
kb_choise.add(KeyboardButton('Добавить Ripple'))

kb_choise_delete = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_choise_delete.add(KeyboardButton('Удалить Tether'))
kb_choise_delete.add(KeyboardButton('Удалить Ripple'))


async def create_keyboard(message: types.Message):
	kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	kb.add(KeyboardButton('Биткоин'))
	kb.add(KeyboardButton('Эфириум'))

	cheeeeeeck = await check_custom_button_tether(user_id=message.from_user.id)
	riple_check = await check_custom_button_ripple(user_id=message.from_user.id)

	if cheeeeeeck == 'Not None':
		kb.add(KeyboardButton('Tether'))

	elif cheeeeeeck == None:
		return kb
	
	if riple_check == 'Not None':
		kb.add(KeyboardButton('Riple'))
	
	elif riple_check == None:
		return kb	

	return kb