#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.core import file_option,log_opt, bill_opt
import json
import time


def transafe(card_num):
    # 转账
    num = input('请输入要转账的卡号：').strip()
    if card_num == num:
        print('给自己转账干毛啊。。。')
    else:
        date = file_option.read()
        print('余额为：', date.get(card_num)[8])
        if date.get(num):
            print('对方姓名为*', date.get(num)[2][-1])
            print('确认转账？y/n')
            c = input(':').strip()
            if c == 'y':
                money = input('输入金额').strip()
                if money.isdigit():
                    money = int(money)
                    if money < date.get(card_num)[8]:
                        date[card_num][8] -= money
                        date[num][8] += money
                        file_option.write(json.dumps(date))
                        log_opt.info(card_num + ': transafe '+num+' '+str(money))
                        bill_opt.info(card_num, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 转出：' + str(money))
                        print('转账成功，余额为：', date[card_num][8])
                    else:
                        print('没有那么多钱了。')
                else:
                    print('输入有误。')
        else:
            print('卡号不存在')
