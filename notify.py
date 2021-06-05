import requests
import json
Pincode=int(input("Enter the pincode in ypur area:"))
date=(input("Enter the date:"))
x = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={Pincode}&date={date}")
raw_json=x.json()
for i in range(len(raw_json['centers'])):
    print(raw_json['centers'][i]["name"])
