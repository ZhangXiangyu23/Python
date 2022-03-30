# coding:utf-8

import json
import multiprocessing
import time

class Work(object):
    def __init__(self, q):
        self.q = q

    def send(self, message):
        if not isinstance(message, str):
            message = json.dumps(message)
        self.q.put(message)

    def send_all(self):
        for i in range(20):
            self.q.put(i)
            time.sleep(1)


    def receive(self):
        while 1:
            # 获取到队列中的消息
            result = self.q.get()
            try:
                # 反序列化
                res = json.loads(result)
            except:
                res = result
            print("receive is %s" % res)



if __name__ == "__main__":
    # 队列
    q = multiprocessing.Queue()
    # 实例化work类
    work = Work(q)
    # 给send函数开一个进程
    send = multiprocessing.Process(target=work.send, args=({'name': 'zxy'},))
    # 给recv函数开一个进程
    recv = multiprocessing.Process(target=work.receive)

    send.start()
    recv.start()

    send.join()
    # 终止recv进程
    recv.terminate()