import requests
import base64
import xml.etree.ElementTree as ET
from colorama import Fore
from pyfiglet import Figlet
import webbrowser
import requests, os, sys, time, pyfiglet

jo1 = '\033[1;31m'  # احمر
jo2 = '\033[1;33m'  # اصفر
jo3 = '\033[2;32m'  # اخضر
jo4 = "\033[1;97m"  # ابيض
jo5 = '\033[2;36m'  # سمائي
jo6 = '\033[1;34m'  # ازرق فاتح.
jo7 = "\033[1;97m"  # ابيض
jo8 = '\033[1;31m'
jo9 = '\033[2;36m'
jo10 = '\033[1;32m'
jo11 = '\033[1;33m'
Jo = pyfiglet.figlet_format("El Jo Net")
print(jo1 + Jo)
webbrowser.open("https://t.me/ELJoNeT208")
jo12 = input(jo3 + "ENTER a Email : " + jo5)
print("")
jo13 = input(jo3 + "ENTER a Password : " + jo5)
print("")
jo14 = input(jo3 + "Enter a Number : " + jo5)
m=int(input("Entar a repeat : "))
for _ in range(m):

    if "01" in jo14:
        jo15 = jo14[+1:]
    else:
        jo15 = jo14

    jo16 = jo12 + ":" + jo13
    jo17 = jo16.encode("ascii")
    jo18 = base64.b64encode(jo17)
    jo19 = jo18.decode("ascii")
    jo20 = "Basic" + " " + jo19

    jo21 = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"

    jo22 = {
        "applicationVersion": "2",
        "applicationName": "MAB",
        "Accept": "text/xml",
        "Authorization": jo20,
        "APP-BuildNumber": "964",
        "APP-Version": "27.0.0",
        "OS-Type": "Android",
        "OS-Version": "12",
        "APP-STORE": "GOOGLE",
        "Is-Corporate": "false",
        "Content-Type": "text/xml; charset=UTF-8",
        "Content-Length": "1375",
        "Host": "mab.etisalat.com.eg:11003",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/5.0.0-alpha.11",
        "ADRUM_1": "isMobile:true",
        "ADRUM": "isAjax:true"
    }

    jo23 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
    jo24 = requests.post(jo21, headers=jo22, data=jo23)

    if "true" in jo24.text:
        st = jo24.headers["Set-Cookie"]
        ck = st.split(";")[0]
        br = jo24.headers["auth"]

        jo25 = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/offersV3?req=<dialAndLanguageRequest><subscriberNumber>%s</subscriberNumber><language>1</language></dialAndLanguageRequest>" % (jo15)

        jo26 = {
            'applicationVersion': "2",
            'Content-Type': "text/xml",
            'applicationName': "MAB",
            'Accept': "text/xml",
            'Language': "ar",
            'APP-BuildNumber': "10459",
            'APP-Version': "29.9.0",
            'OS-Type': "Android",
            'OS-Version': "11",
            'APP-STORE': "GOOGLE",
            'auth': "Bearer " + br,
            'Host': "mab.etisalat.com.eg:11003",
            'Is-Corporate': "false",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'User-Agent': "okhttp/5.0.0-alpha.11",
            'Cookie': ck
        }

        jo27 = requests.get(jo25, headers=jo26)

        if jo27.status_code == 200:
            root = ET.fromstring(jo27.text)
            jo28 = None
            for category in root.findall('.//mabCategory'):
                for product in category.findall('.//mabProduct'):
                    for parameter in product.findall('.//fulfilmentParameter'):
                        if parameter.find('name').text == 'Offer_ID':
                            jo28 = parameter.find('value').text
                            break
                    if jo28:
                        break
                if jo28:
                    break
        else:
            print(jo6 + "هذا العرض غير متاح ، حاول بكره ")

    else:
        print(jo1 + "الحساب غير صحيح")

    if "true" in jo24.text:
        st = jo24.headers["Set-Cookie"]
        ck = st.split(";")[0]
        br = jo24.headers["auth"]

        jo29 = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/submitOrder"

        jo30 = {
            "applicationVersion": "2",
            "applicationName": "MAB",
            "Accept": "text/xml",
            "Cookie": ck,
            "Language": "ar",
            "APP-BuildNumber": "964",
            "APP-Version": "27.0.0",
            "OS-Type": "Android",
            "OS-Version": "12",
            "APP-STORE": "GOOGLE",
            "auth": "Bearer " + br + "",
            "Is-Corporate": "false",
            "Content-Type": "text/xml; charset=UTF-8",
            "Content-Length": "1375",
            "Host": "mab.etisalat.com.eg:11003",
            "Connection": "Keep-Alive",
            "User-Agent": "okhttp/5.0.0-alpha.11"
        }

        jo31 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>ACTIVATE</operation><parameters><parameter><name>GIFT_FULLFILMENT_PARAMETERS</name><value>Offer_ID:%s;ACTIVATE:True;isRTIM:Y</value></parameter></parameters><productName>FAN_ZONE_HOURLY_BUNDLE</productName></submitOrderRequest>" % (
        jo15, jo28)

        jo32 = requests.post(jo29, headers=jo30, data=jo31).text

        if "true" in jo32:
            text4 = "تم اضافه ساعتين سوشيال بنجاح ✅"
            print("")
            print(jo3 + text4)
        else:
            print(jo1 + "بيانات الحساب غير صحيحه ❌")
    else:
        print("")
