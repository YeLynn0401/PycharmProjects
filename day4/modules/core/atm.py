#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
p =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(p)
from modules.core import atm_withdrowal, atm_repayment, atm_transfer, \
    atm_card_apply, atm_login, atm_card_info, atm_management, bill_opt, atm_card_bill

# ATM系统运行时首先运行的方法，将到期的临时账单放到历史账单中。
bill_opt.sss()
def atm():
    login_status = ''
    while True:
        print('欢迎使用中国人民很行ATM服务'.center(30, '-'))
        print('1、信用卡登陆 2、申请信用卡 3、atm管理 q、退出')
        choise = input(':').strip()
        if choise.isdigit():
            choise = int(choise)
            if choise == 1:
                card_num = atm_login.login()
                if card_num:
                    while True:
                        print('欢迎使用ATM，你的卡号是', card_num)
                        print('1、存钱 2、取钱 3、转账 4、还款 5、查看账户信息 6、查看账单 b、返回 q、退出')
                        choise1 = input(':').strip()
                        if choise1.isdigit():
                            if choise1 == '1':
                                atm_repayment.repay(card_num)
                            elif choise1 == '2':
                                atm_withdrowal.withdrowal(card_num)
                            elif choise1 == '3':
                                atm_transfer.transafe(card_num)
                            elif choise1 == '4':
                                atm_repayment.repay(card_num)
                            elif choise1 == '5':
                                atm_card_info.info(card_num)
                            elif choise1 == '6':
                                atm_card_bill.info(card_num)
                            else:
                                print('error')
                        else:
                            if choise1 == 'q':
                                print('bye......')
                                exit()
                            elif choise1 == 'b':
                                break
                            else:
                                print('输入错误。')

            elif choise == 2:
                user_info = atm_card_apply.apply()
            elif choise == 3:
                atm_management.manage()
            else:
                print('输入错误')
        else:
            if choise == 'q':
                print('bye......')
                break
            else:
                print('输入错误。')