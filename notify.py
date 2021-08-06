import requests
import json
from twilio.rest import Client
import time
import datetime

PINCODE = "226010"
DATE = str((datetime.date.today() + datetime.timedelta(1)).strftime('%d-%m-%Y'))
url=f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date="+DATE
header={'User-Agent':'application/json; charset=utf-8'}

def dose():
    response = requests.get(url, headers={}, data={})
    Json = json.loads(response.text)
    if Json and int(Json['centers'][0]['sessions'][0]['available_capacity_dose1']) > 0:
        dose_message = "Available dose:", Json['centers'][0]['name'], Json['centers'][0]['sessions'][0]['available_capacity_dose1'], "available_slots:", Json['centers'][0]['sessions'][0]['slots']
    else:
        dose_message = ""
    return dose_message



def notify(dose_message):
    account_sid ='AC1118249bbb713f8e117a9cfb1f9f982d'
    auth_token ='28dea20cf6c8e6e6872dad81a5bfdfb0'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f"{dose_message}",
        to='+918931039359'
        #to=['whatsapp:+918931039359','whatsapp:+919919017100'],



    )



dose_message=dose()
if dose_message:
    notify(dose_message)
    while (dose_message):
        time.sleep(8)
        dose_message = dose()
        notify(dose_message)
        dose_message =""
    notify("All slots are booked now ... did you booked or missed it ??")
else:
    print(" ")