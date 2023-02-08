import sqlite3
from data.config import database

async def db_start():
	global db, cur

	db = sqlite3.connect(database)
	cur = db.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS profile (
		user_id TEXT primary key,
		full_name TEXT,
		first_name TEXT,
		user_name TEXT,
		cm_btn_tether TEXT,
		cm_btn_ripple TEXT
		)""")

	db.commit()

async def create_profile(user_id, full_name, first_name, user_name):
	user = bool(cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone())
	print(user)
	if user == False:
		cur.execute("""INSERT INTO profile ('user_id', 'full_name', 'first_name', 'user_name') 
			VALUES(?, ?, ?, ?)""", (user_id, full_name, first_name, user_name))
		db.commit()
	
	else:
		print('Пользователь имеется в бд')

async def check_custom_button_tether(user_id):
	cm_btn_1 = cur.execute("SELECT cm_btn_tether FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
	check = cm_btn_1[0]
	return check

async def check_custom_button_ripple(user_id):
	cm_btn_2 = cur.execute("SELECT cm_btn_ripple FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
	check_2 = cm_btn_2[0]
	return check_2

async def button_tether_update(user_id):
	cur.execute("UPDATE profile SET cm_btn_tether = ? WHERE user_id = ?", ('Not None', user_id))
	db.commit()

async def button_riple_update(user_id):
	cur.execute("UPDATE profile SET cm_btn_ripple = ? WHERE user_id = ?", ('Not None', user_id))
	db.commit()

async def button_tether_update_delete(user_id):
	cur.execute("UPDATE profile SET cm_btn_tether = ? WHERE user_id = ?", (None, user_id))
	db.commit()

async def button_riple_update_delete(user_id):
	cur.execute("UPDATE profile SET cm_btn_ripple = ? WHERE user_id = ?", (None, user_id))
	db.commit()