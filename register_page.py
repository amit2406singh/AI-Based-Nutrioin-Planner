import tkinter as tk
from tkinter import messagebox

from streamlit.user_info import logout
from auth_system import register_user

def register():

    username = username_entry.get()
    password = password_entry.get()
    age = age_entry.get()
    height = height_entry.get()
    weight = weight_entry.get()

    result = register_user(username,password,age,height,weight)

    messagebox.showinfo("Info",result)


def open_register():

    window = tk.Toplevel()
    window.title("Register User")
    window.geometry("400x400")

    tk.Label(window,text="Register New User",font=("Arial",18)).pack(pady=10)

    tk.Label(window,text="Username").pack()
    global username_entry
    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(window,text="Password").pack()
    global password_entry
    password_entry = tk.Entry(window,show="*")
    password_entry.pack()

    tk.Label(window,text="Age").pack()
    global age_entry
    age_entry = tk.Entry(window)
    age_entry.pack()

    tk.Label(window,text="Height (cm)").pack()
    global height_entry
    height_entry = tk.Entry(window)
    height_entry.pack()

    tk.Label(window,text="Weight (kg)").pack()
    global weight_entry
    weight_entry = tk.Entry(window)
    weight_entry.pack()

    tk.Button(window,text="Register",command=register).pack(pady=10)
logout_button = tk.Button(window,text="Logout",command=logout)
logout_button.pack()