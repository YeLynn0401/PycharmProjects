#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(p)
from modules.core import atm, shopping
if __name__ == '__main__':
    while True:
        print('welcome')
        print('1、网上银行 2、在线商城 q、退出')
        chiose = input().strip()
        if chiose == '1':
            atm.atm()
        elif chiose == '2':
            shopping.shop()
        elif chiose == 'q':
            print('bye...')
            break
        else:
            print('输入有误')
