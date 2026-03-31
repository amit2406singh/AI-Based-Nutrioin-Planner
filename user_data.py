import pandas as pd

def save_user(weight,height,age,calories):

    data = {
        "Weight":[weight],
        "Height":[height],
        "Age":[age],
        "Calories":[calories]
    }

    df = pd.DataFrame(data)

    df.to_csv("users_history.csv",mode="a",index=False,header=False)