import tkinter as tk
import pandas as pd

def open_database():

    window = tk.Toplevel()
    window.title("Food Nutrition Database")
    window.geometry("400x400")

    data = pd.read_csv("nutrition_data.csv")

    tk.Label(window, text="Food Search", font=("Arial",16)).pack(pady=10)

    tk.Label(window, text="Enter Food Name").pack()
    food_entry = tk.Entry(window)
    food_entry.pack()

    result = tk.Label(window, text="")
    result.pack(pady=20)

    def search_food():

        food = food_entry.get()

        food_data = data[data["Food"].str.lower() == food.lower()]

        if not food_data.empty:
            row = food_data.iloc[0]

            result.config(
                text=f"Calories: {row['Calories (kcal)']} kcal\n"
     f"Protein: {row['Protein (g)']} g\n"
     f"Carbs: {row['Carbs (g)']} g\n"
     f"Fat: {row['Fat (g)']} g\n"
     f"Type: {row['Type']}"
            )
        else:
            result.config(text="Food not found")

    tk.Button(window, text="Search", command=search_food).pack(pady=10)