import requests
import json
from twilio.rest import Client
import time

PINCODE = "201301"
DATE = "15-06-2021"
url=f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={DATE}"
header={'User-Agent':'application/json; charset=utf-8'}


def dose():

    response = requests.get(url, headers={}, data={})
    Json = json.loads(response.text)
    if Json and int(Json['centers'][0]['sessions'][0]['available_capacity_dose1'])>0:
        dose_message="Available dose:", Json['centers'][0]['sessions'][0]['available_capacity_dose1'],"available_slots:",Json['centers'][0]['sessions'][0]['slots']
        return dose_message
    else:
        dose_message1 = ""
        #print(dose_message)
        return dose_message1



def notify(dose_message):
    account_sid = 'AC1118249bbb713f8e117a9cfb1f9f982d'
    auth_token = 'ebb94830e2b2615c737c8664681ee22b'
    client = Client(account_sid, auth_token)

    message= client.messages.create(
        from_='whatsapp:+14155238886',
        body=f"Available dose are{dose_message}book your slot now ",
        to='whatsapp:+918931039359'

    )


dose_message=dose()
if dose_message:
   notify(dose_message)
else:
    notify(dose_message)
while (notify(dose_message)!=True):
    time.sleep(10)

