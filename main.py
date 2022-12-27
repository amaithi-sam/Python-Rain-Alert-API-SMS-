
from twilio.rest import Client
import requests

#------------------Twilio API -----------

account_sid = ""
auth_token = ""

#-------------------Open weathermap API----------
open_weather_Endpoint = "https://api.openweathermap.org"
api_key = ""

parameter = {"lat": ,
             "lon": ,
             "appid": api_key,
             "exclude": "current,minutely,daily"

}


response = requests.get(open_weather_Endpoint, params=parameter)

weather_data = response.json()
response.raise_for_status()

weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour in weather_slice:
    condition_code = hour['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's Going to rain today. Remember to bring umbrella ☂ ️..Twilio Sample _amaithi",
        from_='',
        to=''
    )
    print(message.status)



#print(list)


