#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


# _*_coding:utf-8_*_

import pika, time
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(20)
    print(" [x] Done")
    print("method.delivery_tag", method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_consume(callback,
                      queue='task_queue',
                      no_ack=True
                      )
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
