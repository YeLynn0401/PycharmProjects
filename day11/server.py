#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import pika
import sys
import socket
import subprocess

connection = pika.BlockingConnection(pika.ConnectionParameters(host='59.110.166.147'))
channel = connection.channel()
# channel.queue_declare(queue='rpc_queue')
channel.exchange_declare(exchange='logs', type='fanout')
localIP = socket.gethostbyname(socket.gethostname())
result = channel.queue_declare(exclusive=True)  # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

def on_request(ch, method, props, body):
    send_body = 'aa'
    print(body.decode())
    date_list = body.decode().split('--host')
    if len(date_list) == 2:
        ip_list = date_list[1].split()
        if localIP in ip_list:
            a = re.search('run\s+\"(.+)\"', date_list[0])
            comm = a.groups()[0]
            print(comm)
            obj = subprocess.Popen(comm, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            try:
                date = obj.stdout.read()
            except Exception as e:
                date = obj.stderr.read()
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

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue=queue_name, no_ack=True)
print('RPC Running ……')
channel.start_consuming()
