import tkinter as tk
from login_page import open_login

root = tk.Tk()
root.title("AI Nutrition Recommendation System")
root.geometry("400x300")
root.configure(bg="#f5f6fa")

open_login(root)

root.mainloop()