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


# Check if login token exists
TOKEN_FILE = open("token.txt", "r")
TINDER_TOKEN = TOKEN_FILE.read()
TOKEN_FILE.close()

# Login to tinder
if not TINDER_TOKEN:
    PHONE_NUMBER = input('Please enter your phone number under the international format (country code + number): ')

    if send_otp_code(PHONE_NUMBER):
        OTP_CODE = input('Please enter the code you\'ve received by sms: ')
        REFRESH_TOKEN = get_refresh_token(OTP_CODE, PHONE_NUMBER)
        TINDER_TOKEN = get_api_token(REFRESH_TOKEN)
        if TINDER_TOKEN:
            print("tinder token: %s" % TINDER_TOKEN)
            # Save token
            TOKEN_FILE = open("token.txt", "w")
            TOKEN_FILE.write(TINDER_TOKEN)
            TOKEN_FILE.close()

else:
    pass
