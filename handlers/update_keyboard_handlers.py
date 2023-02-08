from aiogram import types, Dispatcher
from create_bot import bot, dp
from database.database import check_custom_button_ripple, check_custom_button_tether, button_tether_update_delete, button_riple_update_delete, button_tether_update, button_riple_update
from keyboard import kb_choise, kb_choise_delete


"""----------------------------------ДОБАВЛЕНИЕ КНОПОК ПОЛЬЗОВАТЕЛЕМ---------------------------------------"""
@dp.message_handler(text='Добавить валюту')
async def add_cash(message: types.Message):
	await bot.send_message(message.from_user.id, text='Выбери какую валюту ты хочешь добавить', reply_markup=kb_choise)



@dp.message_handler(text='Добавить Tether')
async def add_cash_tether(message: types.Message):
	check_tether = await check_custom_button_tether(user_id=message.from_user.id)
	print(check_tether)
	
	if check_tether == None:
		await button_tether_update(user_id=message.from_user.id)
		await bot.send_message(message.from_user.id, text='Вы добавили в клавиатуру эту валюту!')
		

	elif check_tether == 'Not None':
		await bot.send_message(message.from_user.id, text='Данная валюта уже есть в вашей клавиатуре!')



@dp.message_handler(text='Добавить Ripple')
async def add_cash_ripple(message: types.Message):
	riple_check = await check_custom_button_ripple(user_id=message.from_user.id)
	print(riple_check)
	
	if riple_check == None:
		await button_riple_update(user_id=message.from_user.id)
		await bot.send_message(message.from_user.id, text='Вы добавили в клавиатуру эту валюту!')
		

	elif riple_check == 'Not None':
		await bot.send_message(message.from_user.id, text='Данная валюта уже есть в вашей клавиатуре!')
"""----------------------------------ДОБАВЛЕНИЕ КНОПОК ПОЛЬЗОВАТЕЛЕМ---------------------------------------"""


	
"""----------------------------------УДАЛЕНИЕ КНОПОК ПОЛЬЗОВАТЕЛЕМ---------------------------------------"""
@dp.message_handler(text='Удалить валюту')
async def del_cash(message: types.Message):
	await bot.send_message(message.from_user.id, text='Выбери какую валюту ты хочешь удалить', reply_markup=kb_choise_delete)

@dp.message_handler(text='Удалить Tether')
async def del_cash_tether(message: types.Message):
	cheeeeeeck = await check_custom_button_tether(user_id=message.from_user.id)
	print(cheeeeeeck)
	
	if cheeeeeeck == 'Not None':
		await button_tether_update_delete(message.from_user.id)
		await bot.send_message(message.from_user.id, text='Вы удалили данную валюту!')
		

	elif cheeeeeeck == None:
		await bot.send_message(message.from_user.id, text='Этой валюты уже нет в вашей клавиатуре!')



@dp.message_handler(text='Удалить Ripple')
async def del_cash_ripple(message: types.Message):
	riple_check = await check_custom_button_ripple(user_id=message.from_user.id)
	print(riple_check)
	
	if riple_check == 'Not None':
		await button_riple_update_delete(user_id=message.from_user.id)
		await bot.send_message(message.from_user.id, text='Вы удалили данную валюту!')
		

	elif riple_check == None:
		await bot.send_message(message.from_user.id, text='Этой валюты уже нет в вашей клавиатуре!')

"""----------------------------------УДАЛЕНИЕ КНОПОК ПОЛЬЗОВАТЕЛЕМ---------------------------------------"""


def register_handler_update_keyboard(dp: Dispatcher):
	dp.register_message_handler(add_cash)
	dp.register_message_handler(add_cash_tether)
	dp.register_message_handler(add_cash_ripple)
	dp.register_message_handler(del_cash)
	dp.register_message_handler(del_cash_tether)
	dp.register_message_handler(del_cash_ripple)


