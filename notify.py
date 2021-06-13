import requests
from twilio.rest import Client
import json
import time
import schedule



def find():
    account_sid = 'AC1118249bbb713f8e117a9cfb1f9f982d'
    auth_token = 'b4cc2dcd1ebef3473d22a84620745383'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Vaccination centers is available in your area click on this link ad book your slot: https://www.pythonanywhere.com/user/sheamusakash/shares/98765e7bc2624281ad62dd3ba08eea07/',
        to='whatsapp:+918931039359'
    )

    print(message.sid)

    PINCODE = "271831"
    while len(PINCODE) != 6:
        PINCODE = input("Enter the pincode fo which you want the status =>")
        if len(PINCODE) < 6:
            print(f"{PINCODE} is shorter then the actual length")
        elif len(PINCODE) > 6:
            print(f"{PINCODE} is longer than the actual length")

    DATE = "07-06-2021"
    x = requests.get(
        f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={DATE}")
    raw_json = x.json()
    Total_centers = len(raw_json['centers'])
    print()
    print("                    <******     RESULTS          ******>                             ")
    print("------------------------------------------------------------------------")
    print(f"date {DATE}  | Pincode:{PINCODE}")
    if Total_centers != 0:
        print(f"Total centers in your area is:{Total_centers}")
    else:
        print(f"No centers in your area/Kindly re-check the pincode")

    print("-------------------------------------------------------------------------")
    print()

    for cent in range(Total_centers):
        print()
        print(f"[{cent + 1}] Center Name:", raw_json['centers'][cent]['name'])
        fee_val = raw_json['centers'][cent]['fee_type']
        print("--------------------------------------------------------------------")
        print("   Date    Vaccine Type   Vaccine Fee  Minimum Age  Available slot")
        print(" -------  -------------   -----------  -----------  --------------")
        this_session = raw_json['centers'][cent]['sessions']

        for _sess in range(len(this_session)):
            print("{0:^12} {1:^12} {2:^13} {3:^14} {4:^16}".format(this_session[_sess]['date'],
                                                                   this_session[_sess]['vaccine'], fee_val,
                                                                   this_session[_sess]
                                                                   ['min_age_limit'],
                                                                   this_session[_sess]['available_capacity']))



while (find()!=True):
    time.sleep(60)





















