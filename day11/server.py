#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import pika
import sys
import socket
import subprocess

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.100.5'))
channel = connection.channel()
# channel.queue_declare(queue='rpc_queue')
channel.exchange_declare(exchange='logs', type='fanout')
# 获取本机IP
localIP = socket.gethostbyname(socket.gethostname())
result = channel.queue_declare(exclusive=True)  # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)


def on_request(ch, method, props, body):
    send_body = ''
    # print(body.decode())
    # 提取IP地址
    date_list = body.decode().split('--host')
    if len(date_list) == 2:
        ip_list = date_list[1].split()
        # print(localIP)
        if localIP in ip_list:
            a = re.search('run\s+[\"|\']{1}(.+)[\"|\']{1}', date_list[0])
            # 筛选命令行中可执行命令
            comm = a.groups()[0]
            # print(comm)
            obj = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            date = obj.stdout.read()
            # 按平台解析字符串编码
            if sys.platform == 'win32':
                s_body = date.decode('gbk')
            else:
                s_body = date.decode()
            send_body = '\n{}\n{}\n{}\n'.format(localIP.center(30, '-'), s_body, ''.center(40, '-'))
    else:
        send_body = 'err...'

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=send_body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue=queue_name, no_ack=False)
print('RPC Running ……')
channel.start_consuming()
