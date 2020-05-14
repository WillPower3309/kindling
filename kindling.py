from tinder_api import (
    send_otp_code,
    get_refresh_token,
    get_api_token
)

print("\033[93m\n\n\t              ▒▒\n\t                  ▒▒\n\t                  ▒▒▒▒▒▒        ▒▒")
print("\t          ▒▒  ▒▒    ▒▒▒▒▒▒\n\t          ▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒\n\t    ▒▒    ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒")
print("\t            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n\t            ▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒\n\t          ▒▒▒▒▒▒░░▒▒░░░░░░▒▒▒▒▒▒")
print("\t          ▒▒▒▒▒▒░░░░░░░░  ░░▒▒▒▒▒▒\n\t          ▒▒▒▒▒▒  ░░    ░░░░▒▒▒▒▒▒")
print("\t          ▒▒▒▒▒▒░░        ░░░░▒▒▒▒\n\t          ▒▒▒▒░░░░          ░░▒▒▒▒")
print("\t            ▒▒░░            ░░▒▒▒▒\n\t            ▒▒░░          ░░▒▒▒▒")
print("\t              ▒▒▒▒        ░░▒▒\n\t                  ▒▒▒▒▒▒▒▒▒▒\n\n")
print("██╗  ██╗██╗███╗   ██╗██████╗ ██╗     ██╗███╗   ██╗ ██████╗")
print("██║ ██╔╝██║████╗  ██║██╔══██╗██║     ██║████╗  ██║██╔════╝")
print("█████╔╝ ██║██╔██╗ ██║██║  ██║██║     ██║██╔██╗ ██║██║  ███╗")
print("██╔═██╗ ██║██║╚██╗██║██║  ██║██║     ██║██║╚██╗██║██║   ██║")
print("██║  ██╗██║██║ ╚████║██████╔╝███████╗██║██║ ╚████║╚██████╔╝")
print("╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝\033[93m\033[0m\n\n")


# Login to tinder
TINDER_TOKEN = None
PHONE_NUMBER = input('Please enter your phone number under the international format (country code + number): ')

if send_otp_code(PHONE_NUMBER):
    OTP_CODE = input('Please enter the code you\'ve received by sms: ')
    REFRESH_TOKEN = get_refresh_token(OTP_CODE, PHONE_NUMBER)
    print("refresh token: %s" % REFRESH_TOKEN)
    TINDER_TOKEN = get_api_token(REFRESH_TOKEN)
    if TINDER_TOKEN:
        print("tinder token: %s" % TINDER_TOKEN)
