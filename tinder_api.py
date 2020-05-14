import requests

from helpers import gen_url


# Define HTTP request headers (emulate iPhone)
HEADERS = {
    'user-agent': 'Tinder/11.4.0 (iPhone; iOS 12.4.1; Scale/2.00)',
    'content-type': 'application/json'
}


def send_otp_code(phone_number):
    # Make request
    request_url = gen_url('auth/sms/send?auth_type=sms')
    response = requests.post(
        request_url,
        data={
            'phone_number': phone_number
        }
    )

    # Check if request succeeded
    if response.status_code != 200:
        print('Send OTP Code ERROR: Non 200 Response')
        return False
    elif not response.json()['data']['sms_sent']:
        print('Send OTP Code ERROR: SMS not sent but request successful, try again in a few minutes')
        return False
    return True


def get_refresh_token(otp_code, phone_number):
    # Make request
    request_url = gen_url('auth/sms/validate?auth_type=sms')
    response = requests.post(
        request_url,
        data={
            'otp_code': otp_code,
            'phone_number': phone_number
        }
    )

    # Check if request succeeded
    if response.status_code != 200:
        print('Get Refresh Token ERROR: Non 200 Response')
        return False
    elif not response.json()['data']['validated']:
        return False
    return response.json()['data']['refresh_token']


def get_api_token(refresh_token):
    # Make request
    response = requests.post(
        gen_url('auth/login/sms'),
        data={
            'refresh_token': refresh_token
        },
        headers=HEADERS
    )
    print(response.json())
    # Check if request succeeded
    if response.status_code != 200:
        print('Get API Token ERROR: Non 200 Response')
        return False
    return response.json()['data']['api_token']
