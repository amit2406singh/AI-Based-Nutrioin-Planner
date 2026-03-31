import tkinter as tk
from tkinter import messagebox
import pandas as pd
from dashboard_page import open_dashboard


def open_login(root):

    frame = tk.Frame(root)
    frame.pack(pady=40)

    tk.Label(frame,text="Login",font=("Segoe UI",18,"bold")).pack(pady=10)

    tk.Label(frame,text="Username").pack()
    username_entry = tk.Entry(frame)
    username_entry.pack()

    tk.Label(frame,text="Password").pack()
    password_entry = tk.Entry(frame,show="*")
    password_entry.pack()


    def login():

        username = username_entry.get().strip()
        password = password_entry.get().strip()

        try:
            users = pd.read_csv("users.csv")

            # remove spaces in column names
            users.columns = users.columns.str.strip()

            # remove spaces in data
            users["username"] = users["username"].astype(str).str.strip()
            users["password"] = users["password"].astype(str).str.strip()

            user = users[
                (users["username"] == username) &
                (users["password"] == password)
            ]

            if not user.empty:
                messagebox.showinfo("Login","Login Successful")
                open_dashboard(root)

            else:
                messagebox.showerror("Login Failed","Invalid Username or Password")

        except Exception as e:
            messagebox.showerror("Error",str(e))


    tk.Button(frame,text="Login",width=20,command=login).pack(pady=10)