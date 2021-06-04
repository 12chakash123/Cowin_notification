import requests
x = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=110096&date=29-06-2021")
print(x.text)
