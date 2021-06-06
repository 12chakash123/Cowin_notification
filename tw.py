# Download the helper library from https://www.twilio.com/docs/python/install
#import twilio

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid ='AC1118249bbb713f8e117a9cfb1f9f982d'
auth_token ='e8fa7b5fccdadaebd25a9482b7ca7b0a'
client = Client(account_sid, auth_token)

message = client.messages.create(

                              body='vaccination slots are available in you area:notify.py',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+918931039359'
                          )

print(message.sid)

