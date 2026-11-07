import sqlite3
class DatabaseHelper:
	def __init__(self, db_name='library_users.db'):
		self.db_name = db_name
		self.init_database()

	def init_database(self):
		"""Initialize the database and create tables if they don't exist."""
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()

		cursor.execute('''
			CREATE TABLE IF NOT EXISTS users (
				user_id INTEGER PRIMARY KEY AUTOINCREMENT,
				first_name TEXT NOT NULL,
				last_name TEXT NOT NULL,
				gender TEXT NOT NULL,
				membership TEXT NOT NULL,
				remarks TEXT
			)
		''')
		conn.commit()
		conn.close()

	def insert_user(self, first_name, last_name, gender, membership, remarks):
		"""Insert a new user into the database."""
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()
		cursor.execute('''
			INSERT INTO users (first_name, last_name, gender, membership, remarks)
			VALUES (?, ?, ?, ?, ?)
		''', (first_name, last_name, gender, membership, remarks))
		user_id = cursor.lastrowid
		conn.commit()
		conn.close()
		return user_id

	def get_user_by_id(self, user_id):
		"""Retrieve a specific user by ID."""
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
		user_data = cursor.fetchone()
		conn.close()
		return user_data

	def get_all_users(self):
		"""Retrieve all users from the database"""
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM users ORDER BY user_id')
		users_data = cursor.fetchall()
		conn.close()
		return users_data

	def update_user(self, user_id, first_name, last_name, gender, membership, remarks):
		"""Update an existing user in the database"""
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()
		cursor.execute(''' UPDATE users SET first_name = ?, last_name = ?, gender = ?, membership = ?, remarks = ? WHERE user_id = ? ''', (first_name, last_name, gender, membership, remarks, user_id))
		rows_affected = cursor.rowcount
		conn.commit()
		conn.close()
		return rows_affected > 0