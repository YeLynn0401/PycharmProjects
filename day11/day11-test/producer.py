import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 创建连接
channel = conn.channel()  # 创建频道
channel.queue_declare(queue='hello', durable=True)  # 绑定管道名称 durable=True启动管道持久化
# 发送消息
user_input = input('>>>:').strip()
channel.basic_publish(exchange='',
                      routing_key='hello',  # 管道名称
                      body='Hello world! ',
                      properties=pika.BasicProperties(delivery_mode=2))
# properties=pika.BasicProperties(delivery_mode=2)消息持久化

conn.close()
