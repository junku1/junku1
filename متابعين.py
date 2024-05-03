import requests
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
Lo = pyfiglet.figlet_format('Insta ')
print(jo1 + Lo)
Jo = pyfiglet.figlet_format("Followers")
Jok=pyfiglet.figlet_format("El Jo Net")
print(jo3 + Jo)
print(jo5+ Jok)
for _ in range(1):
    webbrowser.open("https://t.me/ElJoNet208")
    
def send_follow(username,password,coo1,coo2):
    tragrt=input('ENTAR USERNAME TO SEND FOLLOWERS : '+ jo5)
    cookies = {
    '_ga': 'GA1.2.379003127.1700346804',
    '_gid': 'GA1.2.2030621174.1700346804',
    coo1: coo2,
    }
    headers = {
    'authority': 'instamoda.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://instamoda.org/tools',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    }
    response = requests.get('https://instamoda.org/tools/send-follower', cookies=cookies, headers=headers)
    for cookie_name, cookie_value in response.cookies.items():pass
    cookies = {
    '_ga': 'GA1.2.379003127.1700346804',
    '_gid': 'GA1.2.2030621174.1700346804',
    cookie_name:cookie_value,
    }
    headers = {
    'authority': 'instamoda.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://instamoda.org',
    'referer': 'https://instamoda.org/tools/send-follower',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    }
    params = {
    'formType': 'findUserID',
    }
    data = {
    'username': tragrt,
    }
    response = requests.post('https://instamoda.org/tools/send-follower', params=params, cookies=cookies, headers=headers, data=data)
    id=response.text.split('<input type="hidden" name="userID" value="')[1].split('"')[0]
    cookies = {
    '_ga': 'GA1.2.379003127.1700346804',
    '_gid': 'GA1.2.2030621174.1700346804',
    cookie_name:cookie_value,
    }
    headers = {
    'authority': 'instamoda.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://instamoda.org/tools/send-follower',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
}
    response = requests.get(f'https://instamoda.org/tools/send-follower/{id}', cookies=cookies, headers=headers)
    cookies = {
    '_ga': 'GA1.2.379003127.1700346804',
    '_gid': 'GA1.2.2030621174.1700346804',
    cookie_name:cookie_value,
    }
    headers = {
    'authority': 'instamoda.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://instamoda.org',
    'referer': f'https://instamoda.org/tools/send-follower/{id}',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }
    params = {
    'formType': 'send',
    }
    data = {
    'adet': '300',
    'userID': id,
    'userName': tragrt,
    }
    response = requests.post(
    f'https://instamoda.org/tools/send-follower/{id}',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    )
    if response.json()['status']=='success':
        print(f'DONE SEND 125 FOLLOWES TO @{tragrt} ')
username=input(jo3+'Entar a Username To Login : '+jo5)
password=input(jo3+'Entar a Password  TO Login : '+jo5)
headers = {
    'authority': 'instamoda.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://instamoda.org',
    'referer': 'https://instamoda.org/login',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
params = ''
data = {
    'username': username,
    'password': password,
    'userid': '',
    'antiForgeryToken': '92e040589f9f0237f5ddd02297bbcf92',
}
response = requests.post('https://instamoda.org/login', params=params, headers=headers, data=data)
if response.json()['status']=='success':
    for cookie_name, cookie_value in response.cookies.items():pass
    send_follow(username,password,cookie_name,cookie_value)
else:
    print(response.text)