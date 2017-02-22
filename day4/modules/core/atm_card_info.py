#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.core import file_option


def info(card_num):
    # 打印信用卡信息
    f = file_option.read()
    i = f.get(card_num)
    x =i[8]-i[7]/2 if i[8] >= i[7]/2 else 0
    print('您的卡号为:', card_num)
    print('信用额度:', i[7])
    print('可用额度：', i[8])
    print('可取现额度：', x)
    print('账单日：', i[5])
    print('还款日：', i[6])
