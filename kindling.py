import json

import requests

def gen_url(endpoint):
    return 'https://api.gotinder.com/v2/%s' % endpoint

def login():
    PHONE_NUM = input("Phone number associated with account: ")

    request_url = gen_url('auth/sms/send?auth_type=sms')
    auth_send_request = requests.post(
        request_url,
        data={
            'phone_number': PHONE_NUM
        }
    )

    if auth_send_request.status_code != 200:
        print("ERROR: Non 200 Response")
        exit(0)

    if(auth_send_request.json()['data']['sms_sent']):
        # code sent, prompt user to enter login code
        SMS_CODE = input("Enter the SMS code sent to %s: " % PHONE_NUM)
        request_url = gen_url('auth/sms/validate?auth_type=sms')
        sms_verification_request = requests.post(
            request_url,
            data={
                'otp_code': SMS_CODE,
                'phone_number': PHONE_NUM
            }
        )

        if auth_send_request.status_code != 200:
            print("ERROR: Non 200 Response")
            exit(0)
        else:
            REFRESH_TOKEN = sms_verification_request.json()['data']['refresh_token']
            print(REFRESH_TOKEN)

    else:
        print("Tinder failed to send an SMS to the number specified")
        exit(0)

login()
