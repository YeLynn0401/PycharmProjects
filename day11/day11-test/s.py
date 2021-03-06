#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.100.5'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         # return fib(n - 1) + fib(n - 2)
#         return 'aaa'

def on_request(ch, method, props, body):
    # body 客户端发来的内容
    # response 服务端响应内容
    print(type(body), body.decode())
    n = body.decode()

    print(" [.] fib(%s)" % n)
    response = body.decode()

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()