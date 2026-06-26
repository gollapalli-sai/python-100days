import requests
from twilio.rest import Client

OWM_Endpoint ="OWM_ENDPOINT"
api_key = "API_KEY"
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"

weather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="twilio_number",
        to="mobile_number"
    )
    print(message.status)