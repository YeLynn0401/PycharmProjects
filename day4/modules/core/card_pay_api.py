#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.core import file_opt, atm_login,bill_opt
from modules.core import file_option, log_opt
import json
import time


def pay(name, money):
    # 商城调用信用卡
    f = file_opt.File_Option()
    # print(f.file_read().get(name)[3])   # 卡号
    date = f.file_read()
    card_num = date.get(name)[3]
    if card_num:
        info = file_option.read()
        yue =info.get(card_num)[8]
        if yue >= money:
            info[card_num][8] -= money
            # print(info)
            file_option.write(json.dumps(info))
            log_opt.info(name+': quick pay success')
            bill_opt.info(card_num, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' 商城消费：'+str(money))
            print('扣款成功')
            return 'ok'
        else:
            log_opt.info(name + ': quick pay error')
            print('信用卡余额不足。')
    else:
        print('暂未绑定任何信用卡。')
