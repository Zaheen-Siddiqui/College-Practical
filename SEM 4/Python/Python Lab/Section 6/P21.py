import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ----------------- Database Setup ----------------- #
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
''')
conn.commit()

# ----------------- Functions ----------------- #
def register_user():
    username = reg_username.get().strip()
    password = reg_password.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "All fields are required!")
    else:
        try:
            cursor.execute('INSERT INTO users(username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration Successful!")
            reg_username.delete(0, tk.END)
            reg_password.delete(0, tk.END)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")

def login_user():
    username = login_username.get().strip()
    password = login_password.get().strip()

    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", f"Welcome, {username}!")
        login_username.delete(0, tk.END)
        login_password.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# ----------------- Main Window ----------------- #
root = tk.Tk()
root.title("User Login & Registration")
root.geometry("350x280")
root.resizable(False, False)

style = ttk.Style()
style.configure("TNotebook.Tab", font=('Arial', 12, 'bold'))
style.configure("TButton", font=('Arial', 10))
style.configure("TLabel", font=('Arial', 10))

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# ----------------- Register Tab ----------------- #
reg_tab = ttk.Frame(notebook)
notebook.add(reg_tab, text='Register')

ttk.Label(reg_tab, text="Register New Account", font=('Arial', 14)).pack(pady=10)

ttk.Label(reg_tab, text="Username:").pack(pady=2)
reg_username = ttk.Entry(reg_tab, width=30)
reg_username.pack()

ttk.Label(reg_tab, text="Password:").pack(pady=2)
reg_password = ttk.Entry(reg_tab, width=30, show='*')
reg_password.pack()

ttk.Button(reg_tab, text="Register", command=register_user).pack(pady=10)

# ----------------- Login Tab ----------------- #
login_tab = ttk.Frame(notebook)
notebook.add(login_tab, text='Login')

ttk.Label(login_tab, text="Login to Your Account", font=('Arial', 14)).pack(pady=10)

ttk.Label(login_tab, text="Username:").pack(pady=2)
login_username = ttk.Entry(login_tab, width=30)
login_username.pack()

ttk.Label(login_tab, text="Password:").pack(pady=2)
login_password = ttk.Entry(login_tab, width=30, show='*')
login_password.pack()

ttk.Button(login_tab, text="Login", command=login_user).pack(pady=10)

root.mainloop()
