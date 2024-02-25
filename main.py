
import requests,smtplib,os
from twilio.rest import Client

my_password=os.environ.get("PASSWORD")
my_email="ayan25844@gmail.com"

auth_token = os.environ.get("AUTH_TOKEN")
account_sid = 'AC0d51864571614b1655083a15d47e2efb'

parameter={
    "lat":-6.175110,
    "lon":106.865036,
    "cnt":4,
    "appid":os.environ.get("OWM_API_KEY")
}

weather_data=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameter)

weather_data.raise_for_status()
weather_list=[i["weather"][0]["id"] for i in weather_data.json()["list"]]

for i in weather_list:
    if i<700:

        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"subject:Bring a umbrella\n\nIt's going to rain today. Remember to bring an umbrella")

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella",
            from_='+15169793103',
            to='+911234567890'
        )
        print(message.status)
        break