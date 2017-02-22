#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.core import file_option, log_opt,bill_opt
import json
import time


def repay(card_num):
    # 存款/还款
    date = file_option.read()
    if date.get(card_num):
        m = input('输入金额:').strip()
        if m.isdigit():
            m = int(m)
            if m > 0:
                date[card_num][8] += m
                file_option.write(json.dumps(date))
                log_opt.info(card_num+': repay  '+str(m))
                bill_opt.info(card_num, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 还款：' + str(m))
                print('存款成功，当前可用余额：人民币', date[card_num][8], '元')
            else:
                print('别闹，好好的。')
        else:
            print('别闹，好好的。')
    else:
        print('账户不存在。')
        # TODO 没写完
