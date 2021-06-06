import requests
import tw
import json
PINCODE="271831"
while len(PINCODE)!=6:
    PINCODE=input("Enter the pincode fo which you want the status =>")
    if len(PINCODE)<6:
        print(f"{PINCODE} is shorter then the actual length")
    elif len(PINCODE)>6:
        print(f"{PINCODE} is longer than the actual length")

DATE = "07-06-2021"
x = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={DATE}")
raw_json=x.json()

Total_centers=len(raw_json['centers'])
print()
print("                    <******     RESULTS          ******>                             ")
print("------------------------------------------------------------------------")
print(f"date {DATE}  | Pincode:{PINCODE}")


if Total_centers !=0:
    print(f"Total centers in your area is:{Total_centers}")
else:
    print(f"No centers in your area/Kindly re-check the pincode")

print("-------------------------------------------------------------------------")
print()

for cent in range(Total_centers):
    print()
    print(f"[{cent+1}] Center Name:", raw_json['centers'][cent]['name'])
    fee_val =raw_json['centers'][cent]['fee_type']
    print("--------------------------------------------------------------------")
    print("   Date    Vaccine Type   Vaccine Fee  Minimum Age  Available slot")
    print(" -------  -------------   -----------  -----------  --------------")
    this_session= raw_json['centers'][cent]['sessions']

    for _sess in range(len(this_session)):
        print( "{0:^12} {1:^12} {2:^13} {3:^14} {4:^16}" .format(this_session[_sess]['date'],this_session[_sess]['vaccine'], fee_val,this_session[_sess]
        ['min_age_limit'],this_session[_sess]['available_capacity'] ))
