#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import logging
import datetime


def info(date):
    # 打印ATM系统日志
    logging.basicConfig(filename='system.log',level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info(date)
