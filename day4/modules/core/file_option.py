#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import os
import json
p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path = os.path.join(p, 'db', 'atm')


def card_num():
    # 生成新的卡号
    file_path = os.path.join(path, 'card_count')
    with open(file_path, 'r', encoding='utf-8') as f:
        date = f.read()
        print(date)
        return date


def write(date, *num):
    # 写入信用卡信息文件
    file_path = os.path.join(path, 'card_info')
    file_count_path = os.path.join(path, 'card_count')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(date)
    if num:
        with open(file_count_path, 'w', encoding='utf-8') as n:
            date = n.write(num[0])


def read():
    # 读取信用卡信息文件
    with open(os.path.join(path, 'card_info'), 'r', encoding='utf-8') as f:
        date = f.read()
        return json.loads(date)

