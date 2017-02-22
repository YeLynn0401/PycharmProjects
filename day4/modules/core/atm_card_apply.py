#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
import os
import sys
import json
from modules.core import file_option, log_opt

paa = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))




def apply():
    card_info = {}

    USER_INFO = []
    pwd = ''
    lock = 0
    bill_date = '19'
    repayment_date = '10'
    while True:
        m = 30
        b = 100
        print('欢迎申请中国人民很行信用卡，请填写相关资料，我行审核通过后将给您核发信用卡。')
        name = input('name').strip()
        if name == '':
            print('请输入姓名。')
            continue
        age = input('age').strip()
        if age == '':
            print('请输入年龄。')
            continue
        elif age.isdigit():
            age = int(age)
            if age > 60 or age <18:
                print('您的年龄无法申请信用卡。')
                break
        else:
            print('请输入正确的年龄。')
            continue
        job = input('请选择您的工作：1、实习生 2、工地民工 3、运维工程师 4、开发工程师 5、行政 6、其他').strip()
        if job == '':
            print('请选择职业。')
            continue
        if job.isdigit():
            job = int(job)
        if job == 3:
            m *= 6
            b *= 6
        elif job == 4:
            m *= 8
            b *= 8
        elif job == 1 or job == 2 or job == 5:
            m *= 4
            b *= 4

        if age < 25:
            limit = random.randint(m*30, m*40*2)
        elif age >= 25 and age <= 35:
            limit = random.randint(m*40, m*50*2)
        elif age > 35 and age <= 60:
            limit = random.randint(40000, 50000)



        #
        num = file_option.card_num()
        num = json.loads(num) + 1
        num = json.dumps(num)
        # print(num, type(num))


        # USER_INFO.append(num)  # 卡号
        USER_INFO.append(pwd)  # 密码
        USER_INFO.append(0)  # 密码错误次数
        USER_INFO.append(name)  # 姓名
        USER_INFO.append(age)      # 年龄
        USER_INFO.append(lock)  # 锁定状态
        USER_INFO.append(bill_date) # 账单日
        USER_INFO.append(repayment_date) # 还款日
        USER_INFO.append(limit) # 额度
        USER_INFO.append(limit)  # 余额
        # USER_INFO = json.dumps(USER_INFO)

        card_info = file_option.read()
        card_info[num] = USER_INFO
        card_info = json.dumps(card_info)
        file_option.write(card_info, num)
        bill_path = os.path.join(paa, 'db', 'atm', 'bill', num, 'tmp')  # 创建账户对应的账单文件夹
        os.makedirs(bill_path)
        log_opt.info(num + ': card application success')  # 记录日志
        print(name, '信用卡申请成功，您的信用卡额度为{}'.format(limit))
        print('您的卡号为', num,)
        print('账单日', bill_date, '还款日', repayment_date)
        print('请牢记个人信息，并及时还款。')
        return USER_INFO
