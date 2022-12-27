
from twilio.rest import Client
import requests

#------------------Teilio API -----------

account_sid = "AC26e1b11672f18e66586c15a64e72b07f"
auth_token = "c26fa9ec2712b38bc539f01678d029e3"

#-------------------Open weathermap API----------
open_weather_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a73601fe1feaf29b19870b2a22c9d0e1"

parameter = {"lat": 13.337830,
             "lon": 80.192902,
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
        from_='+18635938887',
        to='+919791430778'
    )
    print(message.status)



#print(list)


