from twilio.rest import Client

ACCOUNT_SID=""
AUTH_TOKEN=""
FROM="whatsapp:+14155238886"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def sendMessage(senderId, message):
    
    res = client.messages.create(
        body=message,
        from_=FROM,
        to=f'whatsapp:+{senderId}')
    return res