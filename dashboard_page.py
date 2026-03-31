import tkinter as tk
from predictor_page import open_predictor
from grok_assistant import open_chat
from nutrition_ai_assistant import search_food


def open_dashboard(root):

    dashboard = tk.Toplevel(root)
    dashboard.title("AI Nutrition Recommendation System")
    dashboard.geometry("500x400")

    title = tk.Label(
        dashboard,
        text="AI Nutrition Recommendation System",
        font=("Arial",18,"bold")
    )
    title.pack(pady=20)

    tk.Button(
        dashboard,
        text="Nutrition Assistant",
        width=25,
        height=2,
        command=lambda: open_predictor(dashboard)
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="Food Search",
        width=25,
        height=2,
        command=lambda: search_food(dashboard)
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="Chat Assistant",
        width=25,
        height=2,
        command=lambda: open_chat(dashboard)
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="Exit",
        width=25,
        height=2,
        command=dashboard.destroy
    ).pack(pady=10)