from twilio.rest import Client

ACCOUNT_SID="ACacfa20d6e409fbefc9cd4c8a61f465af"
AUTH_TOKEN="9c94db95a9b144722b688ab9bb14d792"
FROM="whatsapp:+14155238886"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def sendMessage(senderId, message):
    
    res = client.messages.create(
        body=message,
        from_=FROM,
        to=f'whatsapp:+{senderId}')
    return res