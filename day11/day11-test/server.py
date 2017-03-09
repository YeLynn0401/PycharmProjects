#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 创建连接
channel = conn.channel()  # 声明频道
channel.queue_declare(queue='hello', durable=True)  # 管道名称 durable=True启动管道持久化
channel.basic_publish(exchange='', routing_key='hello', body='hello world',
                      properties=pika.BasicProperties(delivery_mode=2))  # properties=pika.BasicProperties(delivery_mode=2)消息持久化

conn.close()
