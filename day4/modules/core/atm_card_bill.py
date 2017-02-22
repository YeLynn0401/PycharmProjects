#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import os
paa = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def info(card_num):
    # 从文件中读取及打印账单
    list1={}
    temp_bill_path = os.path.join(paa, 'db', 'atm', 'bill', card_num, 'tmp')
    bill_path = os.path.join(paa, 'db', 'atm', 'bill', card_num)

    file_list = os.listdir(bill_path)  # 账单
    file_list.remove('tmp')
    file_list_tmp = os.listdir(temp_bill_path)  # 账单

    if file_list:
        print('已出账单：\n序号\t账单')
        list1 = [(k, v) for k, v in enumerate(file_list)]
        for k, v in list1:
            print(k, v)

    if file_list_tmp:  # 打印未出账单
        print('未出账单：')
        print(file_list_tmp[0])
        print('x：查看未出账单')
    print('已出账单请输入账单序号')
    i = input().strip()
    if i == 'x':
        with open(os.path.join(temp_bill_path, file_list_tmp[0]), 'r', encoding='utf-8') as f:
            date = f.read()
        print(date)

    elif i.isdigit():
        i = int(i)
        if list1[i]:
            with open(os.path.join(bill_path, list1[i][1]), 'r', encoding='utf-8') as f:
                date = f.read()
            print(date)
