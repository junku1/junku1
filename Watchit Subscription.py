import requests
import hashlib
import pyfiglet
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
F = '\033[2;32m'  # اخضر
C = "\033[1;97m"  # ابيض
B = '\033[2;36m'  # سمائي
Y = '\033[1;34m'  # ازرق فاتح.
C = "\033[1;97m"  # ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
import webbrowser
webbrowser.open('https://t.me/ElJoNet208')
ascii_art = pyfiglet.figlet_format('El Jo Net')
mmm = pyfiglet.figlet_format('Watchit')
print(F+ ascii_art)
print(B+ "by code: El Jo ")
print(Y+mmm)
num=input(F+' Enter a Number : '+B)
print("")
pas=input(F+'Enter a Password : '+B)
print("")
url = 'https://services.orange.eg/SignIn.svc/SignInUser'
header = {
    "net-msg-id": "61f91ede006159d16840827295301013",
    "x-microservice-name": "APMS",
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "166",
    "Host": "services.orange.eg",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.14.9",}
data = '{"appVersion":"7.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (
    num, pas)
r = requests.post(url, headers=header, data=data).json()
userid = r["SignInUserResult"]["UserData"]["UserID"]
#print(userid)
urlo = "https://services.orange.eg/GetToken.svc/GenerateToken"
hdo = {"Content-type": "application/json",
       "Content-Length": "78",
       "Host": "services.orange.eg",
       "Connection": "Keep-Alive",
       "User-Agent": "okhttp/3.12.1"}
datao = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (
    num, pas)
ctv = requests.post(urlo, headers=hdo, data=datao).json()["GenerateTokenResult"]["Token"]
key = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
htv = (str(hashlib.sha256((ctv + key).encode('utf-8')).hexdigest()).upper())
url2 = "https://services.orange.eg/APIs/Entertainment/api/EagleRevamp/Fulfillment"
data2 = '{"ChannelName":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF","Dial":"%s","Language":"ar","Password":"%s","ServiceID":"5"}' % (
    num, pas)
header2 = {
    "_ctv": ctv,
    "_htv": htv,
    "net-msg-id": "c9e426a1017474d16840837286861043",
    "x-microservice-name": "APMS",
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "142",
    "Host": "services.orange.eg",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.14.9",}
try:
    r = requests.post(url2, headers=header2, data=data2).json()
    pl = r["ErrorCode"]
    if pl == 0:
        print(F+"تم تفعيل اشتراك Watchit بنجاح،ستصلك رساله بتفاصيل الحساب ✅")
    else:
        print(X+"أنت مشترك في العرض بالفعل")
except requests.exceptions.RequestException as e:
    print(Z+"حدث خطأ في الاتصال، الرجاء، حاول مره تاني ❌")
