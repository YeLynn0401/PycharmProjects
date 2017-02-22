#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import json
import time

import shutil
import logging

datetime.datetime.now().date()
paa = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules.core import file_option
# 如果日期在本月19号0点之后直到下月19号之前的消费记录，存到本月+1.temp文件夹
#
# 如果有超过19号未结算的temp，直接结算


def sss():
    # ATM系统运行时首先运行的方法，将到期的临时账单放到历史账单文件夹中。
    date = file_option.read()
    key = date.keys()
    for i in key:
        bill_path = os.path.join(paa, 'db', 'atm', 'bill', i, 'tmp')
        file_list = os.listdir(bill_path)
        if file_list:
            a = file_list[0]+'_19'
            l = a.split('_')
            # 判断是否到达账单日
            if datetime.datetime.now() > datetime.datetime.now().replace(int(l[0]), int(l[1]), int(l[2])):
                # 到达账单日就把临时文件变成账单
                shutil.move(os.path.join(bill_path,file_list[0]), os.path.join(paa, 'db', 'atm', 'bill', i))


def info(card_num, date):
    # 生成临时账单，记录消费信息
    i = None
    t = time.localtime()
    month = t.tm_mon
    year = t.tm_year
    if t.tm_mday >= 19:
        month += 1
    bill_path = os.path.join(paa, 'db', 'atm', 'bill', card_num, 'tmp', str(year)+'_'+str(month))
    with open(bill_path, 'a', encoding='utf-8') as bl:
        bl.write(date+'\n')

