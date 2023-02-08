from aiogram import types, Dispatcher
from create_bot import bot, dp
from pycoingecko import CoinGeckoAPI
from database.database import check_custom_button_tether, check_custom_button_ripple
from middlewares.throtling import ThrottlingMiddleware
from misc.throtling import rate_limit

cg = CoinGeckoAPI()

@rate_limit(limit=12)
#@dp.message_handler()
async def value_cash(message: types.Message):
	if message.text == 'Биткоин':
		bit_price = cg.get_price(ids='bitcoin', vs_currencies='rub')['bitcoin']['rub']
		await bot.send_message(message.from_user.id, text=f'Стоимость: {bit_price} рублей')

	elif message.text == 'Эфириум':
		ethereum_price = cg.get_price(ids='ethereum', vs_currencies='rub')['ethereum']['rub']
		await bot.send_message(message.from_user.id, text=f'Стоимость: {ethereum_price} рублей')

	elif message.text == 'Tether':
		check_tether = await check_custom_button_tether(user_id=message.from_user.id)
		
		if check_tether == None:
			bot.send_message(message.from_user.id, text=f'У вас нет такой кнопки!')

		elif check_tether == 'Not None':
			tether_price = cg.get_price(ids='tether', vs_currencies='rub')['tether']['rub']
			await bot.send_message(message.from_user.id, text=f'Стоимость: {tether_price} рублей')

	elif message.text == 'Riple':
		riple_check = await check_custom_button_ripple(user_id=message.from_user.id)
		

		if riple_check == None:
			bot.send_message(message.from_user.id, text=f'У вас нет такой кнопки!')

		elif riple_check == 'Not None':
			riple_price = cg.get_price(ids='ripple', vs_currencies='rub')['ripple']['rub']
			await bot.send_message(message.from_user.id, text=f'Стоимость: {riple_price} рублей')
	

def register_value_cash_handler(dp: Dispatcher):
	dp.register_message_handler(value_cash)