# coding:utf-8



"""
    使用多进程模块
"""
import time
import os
import multiprocessing


"""
    使用os.getpid()函数，来获取当前进程号
"""

def work_a():
    for i in range(5):
        print(i, "a", os.getpid())
        time.sleep(1)

def work_b():
    for i in range(5):
        print(i, "b", os.getpid())
        time.sleep(1)


if __name__ == "__main__":
    start_time = time.time()
    # 新开进程
    a_p = multiprocessing.Process(target=work_a)
    b_p = multiprocessing.Process(target=work_b)


    # 利用for循环启动
    for i in (a_p, b_p):
        i.start()

    # join函数进行阻塞
    for i in (a_p, b_p):
        i.join()

    print("耗时:", time.time() - start_time)
    print("主进程为", os.getpid())