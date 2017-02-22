#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.core import file_option, log_opt
import json
import time


# 传入用户名和密码两个参数，
# 返回登陆状态值： error 用户名或密码错误，lock 账号已锁定，success 登陆成功

def login():
    # ATM登陆
    card  = input('卡号：').strip()
    pwd = input('密码：').strip()
    status = ''
    f = file_option.read()
    user_info = f.get(card)
    if user_info:  # 判断用户名是否存在
        if user_info[4] == 1:  # 判断锁定状态
            print('账户被锁定。')
        else:
            if user_info[0] == '':  # 如果没有密码，则为新注册用户，进入激活程序
                while True:
                    print('信用卡未激活')
                    print('b： 返回')
                    time.sleep(1)
                    print('激活信用卡'.center(40,'-'))
                    name = input('请输入申请信用卡时填写的姓名：').strip()
                    if name == user_info[2]:
                        passwd = input('请输入6位数字密码：').strip()
                        if passwd.isdigit() and len(passwd) == 6:
                            user_info[0] = passwd
                            file_option.write(json.dumps(f))
                            log_opt.info(card + ': active success')
                            print('激活成功。')
                            break
                        else:
                            print('请按格式输入。')
                    elif name == 'b':
                        break
                    else:
                        print('请输入申请信用卡时对应的用户名。')
            elif user_info[1] < 3:
                if pwd == user_info[0]:  # 判断密码
                    user_info[1] = 0  # 登陆成功，清空密码错误统计
                    f[card] = user_info
                    file_option.write(json.dumps(f))
                    log_opt.info(card + ': login success')
                    print(card + '登陆成功')
                    status = card
                else:  # 密码错误，将用户信息文件中登陆错误次数+1
                    user_info[1] += 1
                    f[card] = user_info
                    file_option.write(json.dumps(f))
                    log_opt.info(card+ ': pwd error')
                    print('密码错误')
            else:
                print('因密码输入错误次数太多，账户已被暂停使用。')
    else:
        print('卡号不存在')

    return status
