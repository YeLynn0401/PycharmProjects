#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)  # 生成随机queue
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self):
        n = input('>>>:').strip()
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()  # 非阻塞接收
        return self.response


fibonacci_rpc = FibonacciRpcClient()

# print(" [x] Requesting fib(30)")
while True:
    print('action')
    response = fibonacci_rpc.call()
    print(" [.] Got %r" % response.decode())