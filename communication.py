import os
from twilio.rest import Client

account_sid = '<account sid>'
auth_token = '<auth token>'
client = Client(account_sid, auth_token)

contact_list = {'c1':"<contact1>", "c2":"<contact2>","c3":"<contact3>"}

def call(number, msg):
    call = client.calls.create(
                            twiml='<Response><Say>'+msg+'</Say></Response>',
                            to=number ,
                from_= '<twilio number>'
                        )

def sms(number, msg):
	client = Client(account_sid, auth_token)
	client.messages.create(from_= '<twilio number>',
                       	to= number,
                       	body= msg)


def emergency():
	call(contact_list['c3'], "Emergency")

def msg(message):
	sms(contact_list['c3'], message)

		

