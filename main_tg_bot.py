from aiogram import executor
from create_bot import dp
from handlers import currency_handler, main_handlers, update_keyboard_handlers
from middlewares.throtling import ThrottlingMiddleware
from database.database import db_start



async def on_startup(_):
	await db_start()
	dp.middleware.setup(ThrottlingMiddleware())
	print('Бот работает')


main_handlers.register_main_handlers(dp)
currency_handler.register_value_cash_handler(dp)
update_keyboard_handlers.register_handler_update_keyboard(dp)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True, on_startup = on_startup)