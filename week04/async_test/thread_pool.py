# coding:utf-8
import threading
from concurrent.futures import ThreadPoolExecutor
import time

"""
    使用线程池
"""

# 使用线程锁
lock = threading.Lock()


def work(i):
    # 上锁
    lock.acquire()
    print(i)
    time.sleep(1)
    # 解锁
    lock.release()

if __name__ == "__main__":
    t = ThreadPoolExecutor(2)
    for i in range(20):
        t.submit(work, (i, ))


