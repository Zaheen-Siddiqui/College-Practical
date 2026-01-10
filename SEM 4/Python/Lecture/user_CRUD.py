import sqlite3
conn=sqlite3.connect("users.db")
cursor=conn.cursor()

#create a table
cursor.execute("""
	CREATE TABLE IF NOT EXISTS users
	(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		email TEXT UNIQUE NOT NULL,
		age INTEGER NOT NULL
	)
	""")
conn.commit()

#add user
def add_user():
	name=input("ENter name")
	age=input("Enter age")
	email=input("Enter email")
	try:
		cursor.execute("INSERT INTO users(name,email,age) VALUES (?,?,?)",(name,email,age))
		conn.commit()
		print("User added successfully")
	except sqlite3.IntegrityError:
		print("Error:Email is already exist")
		
#show user
def show_user():
	while True:
		print("1.show all users\n2.show name\n3.show age\n4.show email\n5.Exit\n")
		ch=input("Enter your choice")
		if ch=='1':
			cursor.execute("SELECT * from users")
			users=cursor.fetchall()
			if users:
				print("\nList if users")
				print("="*60)
				for user in users:
					print(f"ID:{user[0]},Name:{user[1]}  Email:{user[2]}  Age:{user[3]}")
				
			else:
				print("users not found")
				
		elif ch=='2':
			cursor.execute("SELECT * from users")
			users=cursor.fetchall()
			if users:
				print("\nList if users")
				print("="*60)
				for user in users:
					print(f"Name:{user[1]}")
			else:
				print("users not found")
		elif ch=='3':
			cursor.execute("SELECT * from users")
			users=cursor.fetchall()
			if users:
				print("\nList if users")
				print("="*60)
				for user in users:
					print(f"Age:{user[3]}")
			else:
				print("users not found")
		elif ch=='4':
			cursor.execute("SELECT * from users")
			users=cursor.fetchall()
			if users:
				print("\nList if users")
				print("="*60)
				for user in users:
					print(f"Email:{user[2]}")
			else:
				print("users not found")
		elif ch=='5':
			print("Exiting")
			break
		else:
			print("Invalid choice")
#update user
def update_user():
	user_id=input("Enter uyse id")
	cursor.execute("SELECT * FROM users WHERE id=?",(user_id))
	user=cursor.fetchone()
	if user:
		try:
			new_name=input(f"Enter new name ({user[1]}):")
			new_email=input(f"Enter new email ({user[2]}):")
			new_age=input(f"Enter new age ({user[3]}):")
			
			cursor.execute("UPDATE users SET name=?,email=?,age=? WHERE id=?",(new_name,new_email,new_age,user_id))
			conn.commit()
			print("User updated successfully")
		except sqlite3.IntegrityError:
			print("Error:Email is already exists")
	else:
		print("NO user found")

#delete user
def delete_user():
	user_id=input("Enter uyse id")
	cursor.execute("SELECT * FROM users WHERE id=?",(user_id))
	user=cursor.fetchone()
	if user:
		try:
			cursor.execute("DELETE from users WHERE id=?",(user_id))
			conn.commit()
			print("User deleted successfully")
		except sqlite3.IntegrityError:                 #which exception expected here??
			print("Unexpected error occured")
	else:
		print("User not found")	
		
def search_user():
	user_id=input("Enter user id")
	cursor.execute("SELECT name from users where id=?",(user_id))
	user=cursor.fetchone()
	if user:
		print("User exist")
		for user in users:
			print(f"ID:{user[0]},Name:{user[1]}  Email:{user[2]}  Age:{user[3]}")
	else:
		print("User is not found")
		
	
#menu
while True:
	print("CRUD operations in database")
	print("="*60)
	print("1.Add user\n2.Show users\n3.Update user\n4.Delete user\n5.search user\n6.Exit")
	ch=input("Enter your choice")
	if ch=='1':
		add_user()
	elif ch=='2':
		show_user()
	elif ch=='3':
		update_user()
	elif ch=='4':
		delete_user()
	elif ch=='5':
		search_user()
	elif ch=='6':
		print("Exiting from program")
		break
	else:
		print("Invalid choice")

conn.close()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
