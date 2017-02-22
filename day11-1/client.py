#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import pika

def callback(ch, method, properties, body):
    print('-->', ch, method, properties)
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 向服务器确认处理完成

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 创建连接
channel = conn.channel()  # 声明频道
channel.queue_declare(queue='hello', durable=True)
channel.basic_qos(prefetch_count=1)  # 只处理当前一条信息，处理结束前不再接受新消息
channel.basic_consume(callback, queue='', no_ack=True)  # no_ack=True 不发送确认消息，默认为False，消息未处理完菜，则会调度给其他用户
channel.start_consuming()
