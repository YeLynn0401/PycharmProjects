#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import pika
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# 声明queue
channel.queue_declare(queue='task_queue')
# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
message = ' '.join(sys.argv[1:]) or "Hello World! %s" % time.time()
channel.basic_publish(exchange='', routing_key='task_queue', body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      )
                      )
print(" [x] Sent %r" % message)
connection.close()
