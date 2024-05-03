import requests
import os
import requests
import random
import pyfiglet
import string
from getuseragent import UserAgent
import webbrowser
webbrowser.open('https://t.me/ElJoNet208')
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
red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
m500 = 'https://raw.githubusercontent.com/junku1/junku1/main/500%20%D9%85%D9%8A%D8%AC%D8%A7%20%D8%A7%D9%88%D8%B1%D9%86%D8%AC.py'
spam = 'https://raw.githubusercontent.com/junku1/junku1/main/spam%20whats%20.py'
spam2 = 'https://raw.githubusercontent.com/junku1/junku1/main/spam%20sms.py'
like = 'https://raw.githubusercontent.com/junku1/junku1/main/%D9%84%D9%8A%D9%83%D8%A7%D8%AA%20%D8%A7%D9%86%D8%B3%D8%AA%D8%AC%D8%B1%D8%A7%D9%85.py'
views = 'https://raw.githubusercontent.com/junku1/junku1/main/views%20TiK%20Tok.py'
dvoda = 'https://raw.githubusercontent.com/junku1/junku1/main/data%20nu%20voda%20(jo).py'
Etislat = 'https://raw.githubusercontent.com/junku1/junku1/main/%D8%B3%D8%A7%D8%B9%D8%AA%D9%8A%D9%86%20%D8%A7%D8%AA%D8%B5%D8%A7%D9%84%D8%A7%D8%AA.py'
id = 'https://raw.githubusercontent.com/junku1/junku1/main/%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA.py'
Followers = 'https://raw.githubusercontent.com/junku1/junku1/main/%D9%85%D8%AA%D8%A7%D8%A8%D8%B9%D9%8A%D9%86.py'
Spotify = 'https://raw.githubusercontent.com/junku1/junku1/main/%D8%A7%D8%B4%D8%AA%D8%B1%D8%A7%D9%83spoyifay.py'
def main():
    clear_screen()
    ascii_art = pyfiglet.figlet_format('El Jo Net')
    mmm = pyfiglet.figlet_format('Scripts')
    print(green_color + ascii_art)
    print(light_blue_color + "by code: El Jo ")
    print(Y+mmm)
    print(Z+"""
[1] 500 mega Orange
[2] spam WhatsApp 
[3] spam sms all Network 
[4] Free insta likes 
[5] Free TikTok views 
[6] Vodafone number data 
[7] Two hours of free social Etislat
[8] National ID information 
[9] 125 insta followers for free 
[10] Spotify Orange subscription 
""")
    number = int(input(Y+"Choose the script: "))
    clear_screen()  # مسح الشاشة بعد اختيار المستخدم لرقم
    if number == 1:
        jo = m500
    elif number == 2:
        jo = spam
    elif number == 3:
        jo = spam2
    elif number == 4:
        jo = like
    elif number == 5:
        jo = views
    elif number == 6:
        jo = dvoda
    elif number == 7:
        jo = Etislat
    elif number == 8:
        jo = id
    elif number == 9:
        jo = Followers
    elif number == 10:
        jo = Spotify
    else:
        print("Wrong choice")
        return 

    try:
        response = requests.get(jo)
        response.raise_for_status()
        junku = response.text
        exec(junku)
    except requests.exceptions.RequestException as e:
        print("Error❌❌")

if __name__ == "__main__":
    main()
