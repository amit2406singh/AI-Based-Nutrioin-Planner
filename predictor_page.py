import tkinter as tk
from tkinter import messagebox
from nutrition_ai_assistant import calorie_requirement, macro_prediction, weekly_meal_plan


def open_predictor(parent):

    window = tk.Toplevel(parent)
    window.title("AI Nutrition Health Assistant")
    window.geometry("650x550")
    window.configure(bg="#f5f6fa")

    title = tk.Label(
        window,
        text="AI Nutrition Health Assistant",
        font=("Segoe UI", 16, "bold"),
        bg="#f5f6fa"
    )
    title.pack(pady=10)

    frame = tk.Frame(window, bg="#f5f6fa")
    frame.pack()

    tk.Label(frame,text="Weight (kg)",bg="#f5f6fa").grid(row=0,column=0,padx=10,pady=8)
    weight_entry = tk.Entry(frame)
    weight_entry.grid(row=0,column=1)

    tk.Label(frame,text="Height (cm)",bg="#f5f6fa").grid(row=1,column=0,padx=10,pady=8)
    height_entry = tk.Entry(frame)
    height_entry.grid(row=1,column=1)

    tk.Label(frame,text="Age",bg="#f5f6fa").grid(row=2,column=0,padx=10,pady=8)
    age_entry = tk.Entry(frame)
    age_entry.grid(row=2,column=1)

    tk.Label(frame,text="Food Type",bg="#f5f6fa").grid(row=3,column=0,padx=10,pady=8)

    diet_var = tk.StringVar(value="Veg")
    diet_menu = tk.OptionMenu(frame,diet_var,"Veg","NonVeg")
    diet_menu.grid(row=3,column=1)

    result_box = tk.Text(window,height=18,width=70,font=("Consolas",10))
    result_box.pack(pady=15)

    def run_ai():

        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            age = int(age_entry.get())

            calories = calorie_requirement(age,height,weight)
            protein,carbs,fat = macro_prediction(weight)

            plan = weekly_meal_plan(calories,diet_var.get())

            result_box.delete("1.0","end")

            result_box.insert("end",f"""
Daily Calories Needed : {calories} kcal

Protein : {protein} g
Carbs : {carbs} g
Fat : {fat} g

Weekly Diet Plan
{plan}
""")

        except:
            messagebox.showerror("Input Error","Please enter valid inputs")

    btn = tk.Button(
        window,
        text="Generate AI Diet Plan",
        font=("Segoe UI",11,"bold"),
        bg="#273c75",
        fg="white",
        width=22,
        command=run_ai
    )

    btn.pack(pady=10)