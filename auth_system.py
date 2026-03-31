import pandas as pd
import hashlib

FILE = "users.csv"

# password encryption
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# register new user
def register_user(username, password, age, height, weight):

    data = pd.read_csv(FILE)

    # check if user already exists
    if username in data["username"].values:
        return "User already exists"

    new_user = {
        "username": username,
        "password": hash_password(password),
        "age": age,
        "height": height,
        "weight": weight
    }

    data = pd.concat([data, pd.DataFrame([new_user])], ignore_index=True)

    data.to_csv(FILE, index=False)

    return "User registered successfully"


# login verification
def login_user(username, password):

    data = pd.read_csv(FILE)

    hashed_password = hash_password(password)

    user = data[
        (data["username"] == username) &
        (data["password"] == hashed_password)
    ]

    if not user.empty:
        return True
    else:
        return False