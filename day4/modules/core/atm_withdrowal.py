#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.core import file_option, log_opt, bill_opt
import json
import time


def withdrowal(card_num):
    # 取现
    o = 0
    info = file_option.read()
    m = info[card_num][8]
    i = info[card_num][7]
    if m >= i/2:
        o = m - i/2
    else:
        o = m
    print('当前可用额度：', m, '可取现额度：', o )
    print('信用卡取款收取取款金额的5%手续费。')
    print('最小取款金额为1元')
    p = input('输入取款金额：').strip()
    if p.isdigit():
        p = int(p)
        if p <= o:
            x = p* 0.05
            print('取现手续费', x, '直接从余额中扣除')
            if x < (m - p):
                info[card_num][8] -= p
                info[card_num][8] -= x
                log_opt.info(card_num+': withdrowal   '+str(p))
                file_option.write(json.dumps(info))
                bill_opt.info(card_num, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 取现：' + str(p))
                bill_opt.info(card_num, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 取现手续费：' + str(x))
                print('取款成功。')
            else:
                print('取款数额太大，余额不足以支付手续费')
        else:
            print('没有那么取现额度了，我的哥。')
    else:
        print('输入错误。')
