import re
import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.result_dict = {}
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.100.5'))
        # self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='logs', type='fanout')

    def get_t_id(self, user_task_id):
        user_list = self.result_dict.get(user_task_id)
        if user_list:
            def on_response(ch, method, props, body):
                print(body.decode())

            self.channel.basic_consume(on_response, no_ack=True, queue=user_list[1])
            self.connection.process_data_events()
        else:
            print('dose not have this task_id.')

    def call(self, n):
        # run "fsdfdsf" --host 192.168.1.1
        # 接收到用户输入run, 筛查命令是否合格
        # run "asfsaf" --host 192.168.4.45
        a = re.search('run\s+[\"|\'](.+)[\"|\']\s+\-{2}host\s+(.*)', n)

        try:
            print(a)
            assert a.group() == n
            print(a.groups())
        except:
            print('输入有误，例：run "command" --host HostIP1, HostIP2……')
            return
        # 生成task_id
        temp = str(len(self.result_dict)+1)
        # 生成随机queue
        result = self.channel.queue_declare(exclusive=True)
        callback_queue = result.method.queue
        t_id = str(uuid.uuid4())
        self.result_dict[temp] = [t_id, callback_queue]
        self.channel.basic_publish(exchange='logs',
                                   routing_key='',
                                   properties=pika.BasicProperties(
                                       reply_to=callback_queue,
                                       correlation_id=t_id,
                                   ),
                                   body=n)
        print('task_id:', temp)
        # while self.response is None:
        #     self.connection.process_data_events()
        #     return self.response


fibonacci_rpc = FibonacciRpcClient()
while True:

    user_input = input('>>>:').strip()
    if user_input.startswith('run'):
        fibonacci_rpc.call(user_input)
    elif user_input.startswith('c'):
        task_id = user_input.split('c')[1].strip()
        if task_id.isdigit():
            fibonacci_rpc.get_t_id(task_id)
        else:
            print('输入有误')
    else:
        print('input err')
    # print('i got it:\n', response)
