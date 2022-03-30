# coding:utf-8

import os
import time
import multiprocessing

def work(count):
    print(count, os.getpid())
    time.sleep(5)


if __name__ == "__main__":
    # 进程池
    pool = multiprocessing.Pool(5)
    for i in range(20):
        pool.apply_async(func=work, args=(i, ))

    time.sleep(20)
