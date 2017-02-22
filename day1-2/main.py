#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import json

# pwd = getpass.getpass('pass')
name = input('name:').strip()
pwd = input('pwd:').strip()

def file_option():
    with open('user', 'r', encoding='utf-8') as f:
        date = f.read()
        print(date, type(date))
        date = json.loads(date)
        print(date, type(date))
    return json.loads(date)


def login(name, pwd):
    login_status= []
    date = file_option()
    print(date)
    if date.get(name):
        if pwd == date.get(name)[0]:
            login_status.append(name)
    return login_status

login_status = login(name, pwd)
if login_status:
    print('welcome', login_status[0])