import sqlite3
import re

# ---------- Database Setup ----------
conn = sqlite3.connect('crud_users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')
conn.commit()

# ---------- Helper Functions ----------
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# ---------- CRUD Operations ----------
def add_user():
    try:
        name = input("Enter Name: ").strip()
        email = input("Enter Email: ").strip()

        if not name or not email:
            raise ValueError("Name and Email cannot be empty.")
        if not is_valid_email(email):
            raise ValueError("Invalid email format.")

        cursor.execute('INSERT INTO user(name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        print("✅ User Added Successfully!")
    except sqlite3.IntegrityError:
        print("❌ Error: Email already exists.")
    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

def show_users():
    try:
        cursor.execute('SELECT * FROM user')
        records = cursor.fetchall()
        if records:
            print("\n📋 All Users:")
            for record in records:
                print(f"ID: {record[0]}, Name: {record[1]}, Email: {record[2]}")
        else:
            print("⚠️ No users found.")
    except Exception as e:
        print(f"❌ Error: {e}")

def delete_user():
    try:
        user_id = int(input("Enter User ID to Delete: "))
        cursor.execute('DELETE FROM user WHERE id=?', (user_id,))
        if cursor.rowcount == 0:
            print("⚠️ User ID not found.")
        else:
            conn.commit()
            print("🗑️ User Deleted Successfully!")
    except ValueError:
        print("❌ Please enter a valid numeric User ID.")
    except Exception as e:
        print(f"❌ Error: {e}")

def update_user():
    try:
        user_id = int(input("Enter User ID to Update: "))
        name = input("Enter new Name: ").strip()
        email = input("Enter new Email: ").strip()

        if not name or not email:
            raise ValueError("Name and Email cannot be empty.")
        if not is_valid_email(email):
            raise ValueError("Invalid email format.")

        cursor.execute('UPDATE user SET name=?, email=? WHERE id=?', (name, email, user_id))
        if cursor.rowcount == 0:
            print("⚠️ User ID not found.")
        else:
            conn.commit()
            print("✏️ User Updated Successfully!")
    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except sqlite3.IntegrityError:
        print("❌ Error: Email already exists.")
    except Exception as e:
        print(f"❌ Error: {e}")

def search_user():
    try:
        search_email = input("Enter Email to Search: ").strip()
        if not is_valid_email(search_email):
            raise ValueError("Invalid email format.")

        cursor.execute('SELECT * FROM user WHERE email=?', (search_email,))
        record = cursor.fetchone()
        if record:
            print(f"🔍 Found: ID: {record[0]}, Name: {record[1]}, Email: {record[2]}")
        else:
            print("❌ User not found.")
    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except Exception as e:
        print(f"❌ Error: {e}")

# ---------- Menu ----------
def menu():
    while True:
        print("\n====== User Management Menu ======")
        print("1. Add User")
        print("2. Show All Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Search User by Email")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number from 1 to 6.")
            continue

        if choice == 1:
            add_user()
        elif choice == 2:
            show_users()
        elif choice == 3:
            update_user()
        elif choice == 4:
            delete_user()
        elif choice == 5:
            search_user()
        elif choice == 6:
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid Choice. Please select a valid option.")

# ---------- Run Program ----------
menu()
