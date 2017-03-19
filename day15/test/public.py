#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import pika
import test_5
from sqlalchemy.orm import sessionmaker
import json
session_class = sessionmaker(bind=test_5.engine)
session = session_class()
user_inp = input('请输入关键词：').strip()
data = session.query(test_5.article).filter(test_5.article.article.like('%{}%'.format(user_inp))).all()
if data:
    for i in data:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.100.5'))
        channel = connection.channel()
        channel.exchange_declare(exchange='logs',type='fanout')
        message = json.dumps([i.user, i.article])
        channel.basic_publish(exchange='logs',
                              routing_key='',
                              body=message)
        print(" [x] Sent %r" % message)
        connection.close()

