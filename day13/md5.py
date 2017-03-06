#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# import hashlib
# my_data = '123456'
# my = hashlib.md5()
# my.update(my_data.encode())
# my_md5 = my.hexdigest()
# print(my_md5)
url = 'https://account.youku.com/login/confirm.json?passport=474295701%40qq.com&password=df3192aef281ee9a36a2d43bbd520177&loginType=passport_pwd'
#
# session_requests = requests.session()
import requests
import json
import time


def main():

    username = '474295701@qq.com'
    password = '5211314'

    session = requests.session()

    payload = {
        'passport': username,
        'password': password,
        'captcha': '',
        'remember': '1',
        'callback': 'logincallback_%d' % (time.time() * 1000),
        'from': 'http://login.youku.com/@@@@',
        'wintype': 'page',
    }
    # response = session.post(url='http://account.youku.com/login/', data=payload)
    response = session.get(url=url)
    print(response.text)

    # response = session.post(url='http://vip.youku.com/?c=ajax&a=ajax_do_speed_up')
    # print(json.dumps(response.json(), ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
