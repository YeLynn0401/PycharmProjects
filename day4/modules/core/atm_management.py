#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.core import file_option, log_opt
import json


def manage():
    # 管理ATM  账号：admin  密码：admin
    name = input('name').strip()
    pwd = input('pwd').strip()
    if name == 'admin' and pwd == 'admin':
        log_opt.info('admin :login success')
        while True:
            print('现有用用户列表')
            date = file_option.read()
            for i in date.keys():
                print(i)
            print('b返回首页')
            user_num = input('输入要操作的账号：').strip()
            if user_num in date.keys():
                print('1、调整用户额度2、冻结/解冻用户')
                cho = input().strip()
                if cho == '1':
                    print('当前额度为：', date.get(user_num)[7])
                    o = input('调整为：').strip()
                    if o.isdigit():
                        o = int(o)
                        date[user_num][7] = o
                        file_option.write(json.dumps(date))
                        log_opt.info(user_num + ': quota set:'+str(o))
                        print(user_num, '的额度调整为', o)
                    else:
                        print('输入有误。')
                elif cho == '2':
                    print('1，冻结，2，解冻')
                    c = input().strip()
                    if c == '1':
                        date[user_num][4] = 1
                        file_option.write(json.dumps(date))
                        log_opt.info(user_num+ ': lock')
                        print(user_num, '已冻结')
                    elif c == '2':
                        date[user_num][4] = 0
                        file_option.write(json.dumps(date))
                        log_opt.info(user_num+ ': unlock')
                        print(user_num, '已解冻')
                    else:
                        print('输入有误。')
                else:
                    print('输入有误')
            else:
                if user_num == 'b':
                    break
                else:
                    print('卡号不存在。')
    else:
        print('用户名或密码错误')