import pandas as pd
import random
import tkinter as tk


# Load dataset
data = pd.read_csv("nutrition_data.csv")


# -------------------------
# Calorie Calculation
# -------------------------
def calorie_requirement(age, height, weight):

    calories = (10 * weight) + (6.25 * height) - (5 * age) + 5

    return round(calories)


# -------------------------
# Macronutrients
# -------------------------
def macro_prediction(weight):

    protein = round(weight * 1.5)
    carbs = round(weight * 3)
    fat = round(weight * 0.8)

    return protein, carbs, fat


# -------------------------
# Weekly Meal Plan
# -------------------------
def weekly_meal_plan(calories, diet_type):

    days = [
        "Monday","Tuesday","Wednesday",
        "Thursday","Friday","Saturday","Sunday"
    ]

    foods = data[data["Type"] == diet_type]

    if foods.empty:
        return "No foods found."

    plan = ""

    for day in days:

        breakfast = foods.sample(1)["Food"].values[0]
        lunch = foods.sample(1)["Food"].values[0]
        dinner = foods.sample(1)["Food"].values[0]

        plan += f"""
{day}
Breakfast: {breakfast}
Lunch: {lunch}
Dinner: {dinner}

"""

    return plan


# -------------------------
# Food Search
# -------------------------
def search_food(parent):

    window = tk.Toplevel(parent)
    window.title("Food Search")
    window.geometry("400x400")

    tk.Label(window,text="Search Food").pack(pady=10)

    entry = tk.Entry(window,width=30)
    entry.pack()

    result = tk.Text(window,height=15,width=45)
    result.pack(pady=10)

    def search():

        food = entry.get().lower()

        result.delete("1.0","end")

        foods = data[data["Food"].str.lower().str.contains(food)]

        if foods.empty:
            result.insert("end","Food not found")
        else:
            result.insert("end",foods.head(10).to_string())

    tk.Button(window,text="Search",command=search).pack()