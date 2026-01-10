import tkinter as tk
from tkinter import ttk

#def submit_form:
	

root = tk.Tk()
root.title("Sign-up form")
root.geometry("400x500")
root.resizable(False,False)

tk.Label(root,text = "Name:").pack(anchor = "w",padx=10,pady=2)
name_entry = tk.Enntry(root)
name_entry.pack(fill = "x", padx=10)

tk.Label(root,text = "Address:").pack(anchor = "w",padx=10,pady=2)
address_text = tk.Text(root, height = 3)
address_text.pack(fill = "x", padx=10)

tk.Label(root,text = "Gender:").pack(anchor = "w",padx=10,pady=2)
gender_ty = tk.StringVar(value = "Male")
tk.Radiobutton(root,text = "Male", variable = gender_ty, value = "Male").pack(anchor = "w",padx=20)
tk.Radiobutton(root,text = "Female", variable = gender_ty, value = "Female").pack(anchor = "w",padx=20)

tk.Label(root,text = "Gender:").pack(anchor = "w",padx=10,pady=2)
hobby_reading = tk.BooleanVar()
hobby_sports = tk.BooleanVar()
hobby_travel = tk.BooleanVar()
tk.CheckButton()(rrot, text = "Reading", variable =hobby_reading).pack(anchor = "w",padx=20)
tk.CheckButton()(rrot, text = "Sports", variable =hobby_sports).pack(anchor = "w",padx=20)
tk.CheckButton()(rrot, text = "Travel", variable =hobby_travel).pack(anchor = "w",padx=20)

tk.Label(root,text = "State:").pack(anchor = "w",padx=10,pady=2)
states = ["Maharashtra","MP","Goa","New York","Texas","Florida"]
state_combobox = ttk.Combobox(root,values = states, state = "readonly")
state_combobox.pack(fill = "x", padx=10)
state_combobox.set("Selecte State")

tk.Label(root,text = "Country:").pack(anchor = "w",padx=10,pady=2)
countries = ["India","USA","Canada","UK","Australia"]
country_combobox = ttk.Combobox(root,values = countries, state = "readonly")
country_combobox.pack(fill = "x", padx=10)
country_combobox.set("Selecte Country")

tk.Button(root,text = "Submit", command = submit_form).pack(pady = 10)


