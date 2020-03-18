from twilio.rest import Client
from cridentials import account_sid, auth_token, my_cell, my_twilio
# +1 2073072362

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="yes. it yes time for cheese",
    from_=my_twilio,
    to=my_cell
)

print(message.sid)
