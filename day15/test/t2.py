#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.100.5'))
channel = conn.channel()
channel.queue_declare('hello')


def callback(ch, method, properties, body):
    print(body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)

channel.start_consuming()
