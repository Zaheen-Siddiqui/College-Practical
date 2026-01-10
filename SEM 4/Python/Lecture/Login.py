import tkinter as tk
from tkinter import ttk
import bcrypt

def hash_pass(password):
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt())
def check_pass(hash_pass,user_pass):
    return bcrypt.checkpw(user_pass.encode(),hash_pass)


root = tk.Tk()
root.title("Login Sysytem")
root.geometry("400x500")
root.resizable(False,False)

tk.Label(root,text = "Username:").pack(anchor = "w",padx=10,pady=2)
name = tk.Entry(root)
name.pack(fill = "x", padx=10)

tk.Label(root,text = "Email:").pack(pady=10)
email = tk.Entry(root)
email.pack(pady=10)

tk.Label(root,text = "Password:").pack(anchor = "w",padx=10,pady=2)
password = tk.Entry(root,show="*")
password.pack(pady=10)

tk.Button(root,text = "Register", command = register).pack(pady = 10)

tk.Button(root,text = "login", command = login).pack(pady = 10)

root.mainloop()


def register():
        username = usn_e.get()
        email = em_e.get()
        password = pas_e.get()
        if not username or not password or not email:
            messagebox.showerror("Error","Enter all the values")
            return
        if "@" not in email:
            messagebox.showerror("Error","Enter a valid email")
            return
        if len(password)<6:
            messagebox.showerror("Error","Small Password")
            return
        hashed_pass = hashed_password(password)
        
        try:
            cursor.execute("INSERT INTO users(username, email, password) VALUES (%S,%S,%S)"(username,email,password))
            conn.commit()
            messagebox.showinfo("Success","Registration Succuessful")
        except mysql.connector.iintegrityError:
            messagebox.showerror("Error","Already Exists")
def logoin():
        username = usn_e.get()
        password = pas_e.get()
        
        if not username or not password:
            messagebox.showerror("Error","Enter all the values")
            return
        cursor.execute("SELECT password from users where username = %s",(username))
        user = cursor.fetchone()
        
        if user and check_password (user[0].encode(),password):
             messagebox.showinfo("Suces","Login confirmed")
        else:
            messagebox.showerror("Error","Invalid Username or password")
        