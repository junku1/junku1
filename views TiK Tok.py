import requests
import random
import pyfiglet
import string
from getuseragent import UserAgent
red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'
ascii_art = pyfiglet.figlet_format("El Jo Net")
j = pyfiglet.figlet_format("Tik Tok")
print(green_color + ascii_art)
print(light_blue_color + j)
print(light_blue_color + "by code: El Jo ")
ua = UserAgent('ios').Random()
print("")
link = input(light_green_color + '[+] Post Link: ' + yellow_color)
def generate_username():
    letters = string.ascii_letters
    digits = string.digits
    
    username_letters = ''.join(random.choices(letters, k=10))
    username_digits = ''.join(random.choices(digits, k=5))
    
    return username_letters + username_digits
user = generate_username()
res = requests.post('https://api.likesjet.com/freeboost/3',
                    json={"link": link, "tiktok_username": user, 'email': f'hackyourdata{random.randint(100000, 999999)}@gmail.com'},
                    headers={"Host": "api.likesjet.com",
                             "content-length": "137",
                             "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
                             "accept": "application/json, text/plain, */*",
                             "content-type": "application/json",
                             "sec-ch-ua-mobile": "?1",
                             "user-agent": ua,
                             "sec-ch-ua-platform": "\"Android\"",
                             "origin": "https://likesjet.com",
                             "sec-fetch-site": "same-site",
                             "sec-fetch-mode": "cors",
                             "sec-fetch-dest": "empty",
                             "referer": "https://likesjet.com/",
                             "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5"})

print("")
print(blue_color + res.json()['message'])
