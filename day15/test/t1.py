#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.100.5'))
channel = conn.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='hello world.')
conn.close()
