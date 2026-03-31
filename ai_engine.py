import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("nutrition_data.csv")

# Features
X = data[['Calories (kcal)', 'Protein (g)', 'Carbs (g)', 'Fat (g)']]
y = data['Type']

# Train AI Model
model = DecisionTreeClassifier()
model.fit(X, y)

# BMI Calculation
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi,2)

# AI Food Category Prediction
def predict_food_category(calories, protein, carbs, fat):
    prediction = model.predict([[calories, protein, carbs, fat]])
    return prediction[0]

# AI Food Recommendation
def recommend_foods(calories):
    foods = data[data['Calories (kcal)'] <= calories]
    return foods.head(5)

# Diet Plan Generator
def generate_diet_plan(calories):
    plan = data[data['Calories (kcal)'] < calories]
    return plan.sample(3)

# Health Risk Prediction
def health_risk(bmi):
    if bmi < 18.5:
        return "Underweight Risk"
    elif bmi < 25:
        return "Healthy"
    elif bmi < 30:
        return "Overweight Risk"
    else:
        return "Obesity Risk"