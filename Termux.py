import os
import requests
from time import sleep
import re
from json import loads
ig_did = ''
csrftoken = ''
sessionid = ''
post_id = ''
 
 
def keyFound(dict, key):
    if key in dict.keys():
        return True
    return False
r1 = requests.session()
print("""
 
        Sᴘᴀᴍ & 𝐒𝐞𝐥𝐟
                   
                      𝑩𝒚 @imanzxtesla
                                                                                                                                                                           
                            
""")
username = input("user")
password = input("pass")
Target = input('target')
def login1():
 
    global ig_did, csrftoken, sessionid
 
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    login_headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '275',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=X0padwAEAAEPS5xI4RZu1YV6z7zS; rur=ASH; csrftoken=xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6; urlgen="{\"185.88.26.35\": 201031}:1kC1CG:D41DVXmf-j-T5nYho3c7g7K3MQU"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
        'x-instagram-ajax': '0c15f4d7d44a',
        'x-requested-with': 'XMLHttpRequest'
    }
    login_data = {
        'username': f'{username}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }
    login = r1.post(login_url, data=login_data, headers=login_headers)
    if ('{"user": false, "authenticated": false, "status": "ok"}') in login:
        print("[!] Check Your Username And Try Again")
 
    if ('{"user": true, "authenticated": false, "status": "ok"}') in login.text:
        print("[!] Check Yo Password And Try Again")
 
    if ('{"message": "checkpoint_required"') in login.text:
        print("[!] Checkpoint")
 
    if 'userId' in login.text:
        print("[+] Login Done")
    else:
        print("ERROR pass")
 
    ig_did = login.cookies['ds_user_id']
    csrftoken = login.cookies['csrftoken']
    sessionid = login.cookies['sessionid']
    u = r1.get(f"https://www.instagram.com/{username}/?__a=1")
    idq = str(u.json()["graphql"]["user"]["id"])
    hed = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '31',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'ig_did={ig_did}; mid=X1ej8wALAAH-iuqPdbS2k838raMR; datr=WVVnXzp0tD7mIRdZ-0jb9JKJ; ig_nrcb=1; shbid=14759; shbts=1612285444.666352; rur=ATN; csrftoken={csrftoken}; ds_user_id={idq}; sessionid={sessionid}',
        'origin': 'https://www.instagram.com',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'x-csrftoken': csrftoken,
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR0HH5O9Hioplekd3BZjVgr-KFLmmXjkRtIbTd68b-Ay4U_g',
        'x-instagram-ajax': 'b50ae05deb9f',
        'x-requested-with': 'XMLHttpRequest'
    }
    def spsl():
        u = r1.get(f"https://www.instagram.com/{Target}/?__a=1")
        id = str(u.json()["graphql"]["user"]["id"])
        print(f'{username} > {Target} > {id}')
        urlsp = f'https://www.instagram.com/users/{id}/report/'
        datasp = {
            'source_name': 'profile',
            'reason_id': '1'
        }
        urlsl = f'https://www.instagram.com/users/{id}/report/'
        datasl = {
            'source_name': 'profile',
            'reason_id': '2'
        }
        spp = 0
        sll = 0
        while True:
            spp += 1
            sp = r1.post(urlsp, data=datasp, headers=hed).status_code
            if sp == 200:
                print(f'[+] Spam > {spp}')
            else:
                print(f'[!] Fail Spam ')
            sll += 1
            sl = r1.post(urlsl, data=datasl, headers=hed).status_code
            if sl == 200:
                print(f'[+] Self > {sll}')
            else:
                print(f'[!] Fail Self ')
 
    spsl()
 
login1()