# IMPORTS

import os
import requests
import sys
import subprocess
import json


# GET DATA ON https://authify.biz/
program_key = ""
api_key = ""

def GetUUID():
    if sys.platform == "win32":
        cmd = 'wmic csproduct get uuid'
        uuid = str(subprocess.check_output(cmd))
        pos1 = uuid.find("\\n")+2
        uuid = uuid[pos1:-15]
    else:
        try:
            uuid = os.popen("lscpu | grep -E 'family|cache|Model|Hypervisor|Core|CPU(s)|Architecture|op-mode|Socket|Vendor|Virtualization|Flags'").read()
        except:
            print("Please install util-linux")
    return uuid

if not os.path.exists('auth.json'):
    print("1 Login \n2 Register \n3 Activate \n4 Exit")
    choice = input("Enter your choice >> ")
    if choice == "1":
        username = input('Enter your username >> ')
        password = input('Enter your password >> ')
        hwid = GetUUID()
        auth = requests.get(f"https://authify.biz/api/v1/universal/?type=login&username={username}&password={password}&hwid={hwid}&program_key={program_key}&api_key={api_key}", 
        headers={"User-Agent": "Mozilla Authify"})
        json_data = json.loads(auth.text)
        if json_data['response'] == "program_doesnt_exist":
            print("Initialize failed ask your admin")
            sys.exit()
        if json_data['response'] == "api_key_is_wrong":
            print("Initialize failed ask your admin")
            sys.exit()
        if json_data['response'] == "invalid_username":
            print("Invalid username or password")
            sys.exit()
        if json_data['response'] == "invalid_password":
            print("Invalid username or password")
            sys.exit()
        if json_data['response'] == "no_sub":
            print("No subscription")
            sys.exit()
        if json_data['response'] == "logged_in":
            data = {}
            data = ({
                "username": username,
                "password": password,
                "hwid": hwid
            })
            with open('auth.json', 'w') as outfile:
                json.dump(data, outfile)
            print("Login successful")
    elif choice == "2":
        username = input('Enter your username >> ')
        password = input('Enter your password >> ')
        email = input('Enter your email >> ')
        token = input('Enter your license >> ')
        auth = requests.get(f"https://authify.biz/api/v1/universal/?type=register&username={username}&email={email}&password={password}&token={token}&program_key={program_key}&api_key={api_key}", 
        headers={"User-Agent": "Mozilla Authify"})
        json_data = json.loads(auth.text)
        if json_data['response'] == "program_doesnt_exist":
            print("Initialize failed ask your admin")
            sys.exit()
        if json_data['response'] == "api_key_is_wrong":
            print("Initialize failed ask your admin")
            sys.exit()
        if json_data['response'] == "invalid_email_format":
            print("Invalid email format")
            sys.exit()
        if json_data['response'] == "used_token":
            print("Used token")
            sys.exit()
        if json_data['response'] == "invalid_token":
            print("Invalid token")
            sys.exit()
        if json_data['response'] == "success":
            data = {}
            data = ({
                "username": username,
                "password": password,
                "email": email,
                "token": token
            })
            with open('auth.json', 'w') as outfile:
                json.dump(data, outfile)
            print("Registration successful")
    elif choice == "3":
        username = input('Enter your username >> ')
        password = input('Enter your password >> ')
        token = input('Enter your license >> ')
        auth = requests.get(f"https://authify.biz/api/v1/universal/?type=activate&username={username}&password={password}&token={token}&program_key={program_key}&api_key={api_key}", 
        headers={"User-Agent": "Mozilla Authify"})
        json_data = json.loads(auth.text)
        if json_data['response'] == "program_doesnt_exist":
            print("Initialize failed ask your admin")
            sys.exit()
        if json_data['response'] == "api_key_is_wrong":
            print("Initialize failed ask your admin")
            sys.exit()
        if json_data['response'] == "invalid_username":
            print("Invalid username or password")
            sys.exit()
        if json_data['response'] == "invalid_password":
            print("Invalid username or password")
            sys.exit()
        if json_data['response'] == "invalid_token":
            print("Invalid token")
            sys.exit()
        if json_data['response'] == "used_token":
            print("Used token")
            sys.exit()
        if json_data['response'] == "success":
            data = {}
            data = ({
                "username": username,
                "password": password,
                "token": token
            })
            with open('auth.json', 'w') as outfile:
                json.dump(data, outfile)
            print("Activation successful")
    elif choice == "4":
        sys.exit()
    else:
        print("Invalid choice")
        sys.exit()


