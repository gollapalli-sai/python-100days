import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import smtplib
import pandas as pd  # use alias for clarity

load_dotenv()

# Constants
GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32
MY_EMAIL = "YOUR MAIL"
MY_PASSWORD = "YOUR PASSWORD"  # App password (keep secure!)

# Environment variables
APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]
SHEETY_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["ENV_SHEETY_TOKEN"]

# Input from user
exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API call
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise",
                         json=exercise_params, headers=nutritionix_headers)
result = response.json()
print(f"Nutritionix API call:\n{result}\n")

# Date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Load email addresses from EMAIL.csv
email_df = pd.read_csv("EMAIL.csv")  # assumes a column like "email"
email_list = email_df["email"].tolist()

# Loop through exercises
for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": SHEETY_TOKEN
    }

    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(f"Sheety Response:\n{sheet_response.text}")

    # Send email to all users in EMAIL.csv
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        for email in email_list:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Workout Logged Successfully!\n\n{sheet_response.text}"
            )
