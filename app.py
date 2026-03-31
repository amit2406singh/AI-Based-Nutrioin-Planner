import streamlit as st
from ai_engine import calculate_bmi, calorie_requirement, recommend_food

st.title("AI Personalized Nutrition Planner")

age = st.number_input("Age")
weight = st.number_input("Weight (kg)")
height = st.number_input("Height (cm)")

gender = st.selectbox("Gender",["Male","Female"])

activity = st.selectbox(
"Activity Level",
["Sedentary","Light","Moderate","Active"]
)

diet = st.selectbox("Diet Preference",["Veg","Non-Veg"])

if st.button("Generate Nutrition Plan"):

    bmi = calculate_bmi(weight,height)

    calories = calorie_requirement(age,weight,height,gender,activity)

    food = recommend_food(diet)

    st.subheader("Results")

    st.write("BMI:",bmi)
    st.write("Daily Calories Needed:",calories)

    st.subheader("Recommended Foods")

    st.table(food)