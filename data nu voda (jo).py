import requests
import requests,os,sys,time,pyfiglet
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
Lo=pyfiglet.figlet_format('Yousef Ali ')
print(F+Lo)
Jo=pyfiglet.figlet_format('Data Voda')
print(F+Jo)
print(B+"by code: Youeef Ali ")
nu=input(F+"Enter a number : "+B)
print()
pw=input(F+"Enter a password : "+C)
print()
urlj = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
url="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
url2='https://web.vodafone.com.eg/services/dxl/sam/serviceAccountManagement/v1/serviceAccount?@type=Profile&$.billingAccount.IDs[?(@schemaName%3D%3D%27CustomerID%27)].value=208422279&$.resources[?(@resourceType%3D%3D%27MSISDN%27)].IDs[0].value='+nu
url2m=f'https://web.vodafone.com.eg/services/dxl/usagemng/usage?relatedParty.id={nu}&%40type=ConsumptionDetails&usageSpecification.id=National&$.type%5B0%5D=MI'
urlm="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
data='username='+nu+'&password='+pw+'&grant_type=password&client_secret=a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3&client_id=my-vodafone-app'
datam='username='+nu+'&password='+pw+'&grant_type=password&client_secret=a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3&client_id=my-vodafone-app'
header={
"Accept": "application/json, text/plain, */*",
"Connection": "keep-alive",
"x-agent-operatingsystem": "10.1.0.264C185",
"clientI": "AnaVodafoneAndroid",
"x-agent-device": "HWDRA-MR",
"x-agent-version": "2022.1.2.3",
"x-agent-build": "500",
"Content-Type": "application/x-www-form-urlencoded",
"Content-Length": "142",
"Host": "mobile.vodafone.com.eg",
"User-Agent": "okhttp/4.9.1",}
r=requests.post(url,headers=header,data=data).json()
tok=r["access_token"]
print("Wit...🤌")
header2={"Host": "web.vodafone.com.eg",
"Connection": "keep-alive",
'sec-ch-ua': '"Not)A;Brand"'';v='"24"', '"Chromium"';v="116"',
"msisdn": nu,
"Actept-Language": "EN",
"sec-ch-ua-mobile": "?1",
"Authorization": f"Bearer {tok}",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
"Content-Type": "application/json",
"x-dtpc": "8$452709659_79h7vHFKUEHBLLFOTDFQBHDLNOBETBQNRRHPK-0e0",
"Accept": "application/json",
"clientId": "WebsiteConsumer",
"x-dtreferer": "https://web.vodafone.com.eg/spa/myHome?state=289dcdde-631e-43f9-a030-0eba63364b68&session_state=7879b8bb-1739-4020-93a6-55ddc6ae63af&code=587c22ee-84e7-4be0-aeb6-9fb7da2ae912.7879b8bb-1739-4020-93a6-55ddc6ae63af.b1aeb74f-968a-42c5-892d-acf1725d9a45",
'sec-ch-ua-platform': '"Android"',
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://web.vodafone.com.eg/spa/myHome",
 "Accept-Encoding": "gzip,deflate,br",}
headerm={
"Accept": "application/json, text/plain, */*",
"Connection": "keep-alive",
"x-agent-operatingsystem": "10.1.0.264C185",
"clientI": "AnaVodafoneAndroid",
"x-agent-device": "HWDRA-MR",
"x-agent-version": "2022.1.2.3",
"x-agent-build": "500",
"Content-Type": "application/x-www-form-urlencoded",
"Content-Length": "142",
"Host": "mobile.vodafone.com.eg",
"User-Agent": "okhttp/4.9.1",}
rm=requests.post(urlm,headers=headerm,data=datam).json()
tokm=rm["access_token"]
header2m ={
  "Host": "web.vodafone.com.eg",
  "Connection": "keep-alive",
  "msisdn": nu,
  "Accept-Language": "AR",
  "Authorization": f"Bearer {tokm}",
  "x-dtpc": "5$305993372_560h18vNLSROBPPUFFPBPFRFOIVLUBITPJJBKMB-0e0",
  "Accept": "application/json",
  "User-Agent": "Mozilla/5.0 (Linux; Android 12; CPH2095 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36",
  "clientId": "WebsiteConsumer",
  "Content-Type": "application/json",
  "X-Requested-With": "mark.via.gp",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Dest": "empty",
  "Referer": "https://web.vodafone.com.eg/spa/call-details",
  "Accept-Encoding": "gzip, deflate"}
"""headersj = {
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "x-agent-operatingsystem": "10.1.0.264C185",
    "clientI": "AnaVodafoneAndroid",
    "x-agent-device": "HWDRA-MR",
    "x-agent-version": "2022.1.2.3",
    "x-agent-build": "500",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "142",
    "Host": "mobile.vodafone.com.eg",
    "User-Agent": "okhttp/4.9.1",}
dataj = 'username=' + nu + '&password=' + pw + '&grant_type=password&client_secret=a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3&client_id=my-vodafone-app'
responsej = requests.post(urlj, headers=headersj, data=dataj).json()
tokenj = responsej["access_token"]
url1= 'https://web.vodafone.com.eg/services/dxl/promo/promotion?@type=Promo&$.context.type=WOWRamadan24'
headers1 = {
    "Host": "web.vodafone.com.eg",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"',
    "msisdn": nu,
    "Accept-Language": "AR",
    "sec-ch-ua-mobile": "?1",
    "Authorization": f"Bearer {tokenj}",
    "User-Agent": "vodafoneandroid",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "clientId": "WebsiteConsumer",
    "channel": "WEB",
    "sec-ch-ua-platform": '"Android"',
    "X-Requested-With": "com.emeint.android.myservices",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://web.vodafone.com.eg/portal/bf/wow24",
    "Accept-Encoding": "gzip, deflate, br"}
jo=requests.get(url1, headers=headers1).json()"""
urld= "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
headersd = {
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "x-agent-operatingsystem": "10.1.0.264C185",
    "clientI": "AnaVodafoneAndroid",
    "x-agent-device": "HWDRA-MR",
    "x-agent-version": "2022.1.2.3",
    "x-agent-build": "500",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "142",
    "Host": "mobile.vodafone.com.eg",
    "User-Agent": "okhttp/4.9.1",}
datad = 'username=' + nu + '&password=' + pw + '&grant_type=password&client_secret=a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3&client_id=my-vodafone-app'
responsed = requests.post(urld, headers=headersd, data=datad).json()
tokend = responsed["access_token"]
urls =f'https://mobile.vodafone.com.eg/services/dxl/usagemng/usage?relatedParty.id={nu}&validFor.startDateTime=1710715033253&%40type=BalanceDetails&validFor.endDateTime=1711319833253'
headerss = {
    "api-host": "UsageManagementHost",
    "x-dynatrace": "MT_3_13_3573269726_3-0_a556db1b-4506-43f3-854a-1d2527767923_0_3658_292",
    "Authorization": f"Bearer {tokend}",
    "api-version": "v2",
    "x-agent-operatingsystem": "11",
    "clientId": "AnaVodafoneAndroid",
    "x-agent-device": "OPPO CPH2059",
    "x-agent-version": "2024.3.1",
    "x-agent-build": "591",
    "msisdn": nu,
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Accept-Language": "ar",
    "Host": "mobile.vodafone.com.eg",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.11.0"}
rs=requests.get(urls,headers=headerss).json()
##joo = jo[0]['characteristics'][5]['value']
print("")
r2=requests.get(url2,headers=header2).json()
contact_first_name = r2[0]['contact'][0]['contactFirstName']
contact_last_name = r2[0]['contact'][0]['contactLastName']
service_class = r2[0]['subscriptions'][0]['name']
account_number = r2[0]['billingAccount']['IDs'][1]['value']
customer_id = r2[0]['billingAccount']['IDs'][0]['value']
city = r2[0]['contact'][0]['contactMedium'][0]['city']
print(f"الاسم الأول: {contact_first_name}")
print("")
print(f"الاسم الأخير: {contact_last_name}")
print("")
print(f" نظام الخط: {service_class}")
print("")
print(f"Account Number: {account_number}")
print("")
print(f"Customer ID: {customer_id}")
print("")
print(f"المحافظه: {city}")
print("")
#print(joo+" ; تاريخ شراء الخط")
print("")
print("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»")
print("")
increases = []
for item in rs:
    if item["ratedProductUsage"][0]["taxIncludedRatingAmount"] > 0:
        increase_details = {
            "تاريخ": item["date"],
            "المبلغ": item["ratedProductUsage"][0]["taxIncludedRatingAmount"],
            "الوصف": item["description"]
        }
        increases.append(increase_details)

print("")
print("عمليات الشحن خلال شهر 👇🏻👇🏻")
print("")
print("-" * 50) 
print("تاريخ\t\tالمبلغ        \t\tالوصف   ")
print("-" * 50) 

for increase in increases:
    print(f"{increase['تاريخ']}\t{   increase['المبلغ']}\t\t{increase['الوصف']}")
    print("-" * 50) 
print("@Jo_ViP")