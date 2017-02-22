#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules.core import file_opt, atm_login, log_opt
# import file_opt, atm_login


def bind(name):
    # 商城绑定信用卡
    f = file_opt.File_Option()
    date = f.file_read()
    if date.get(name)[3] == 0:
        card_num = atm_login.login()
        if card_num:
            date[name][3] = card_num
            f.file_write(date)
            log_opt.info(name +':bind'+card_num)
            print('绑定成功。')
    else:
        print('已绑定信用卡：', date.get(name)[3])

