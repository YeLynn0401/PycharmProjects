import pika


def callback(ch, method, properties, body):
    print('-->', ch, method, properties)
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动向服务器发送ack确认处理完成

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 创建连接
channel = conn.channel()  # 创建频道
# channel.queue_declare(queue='amq.gen-MQjRfv0y-x6TTAq3Z9wR2w', durable=True)  # 绑定管道名称 启动管道持久化
# channel.basic_qos(prefetch_count=1)  # 只处理当前一条信息，处理结束前不再接受新消息
channel.basic_consume(callback, queue='amq.gen-MQjRfv0y-x6TTAq3Z9wR2w', no_ack=False)
# no_ack=True 自动发送确认消息，默认为False，消息未处理完成或者未收到ack消息，则会调度给其他用户
channel.start_consuming()  # 开始接收消息（死循环/阻塞）
