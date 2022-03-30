# coding:utf-8

"""
    线程的使用
"""

import random
import time
import threading
lists = ["python", "django", "flask", "java", "c++"]
new_list = []

def work():
    if len(lists) == 0:
        return
    data = random.choice(lists)
    lists.remove(data)
    new_data = "%s_new" % data
    new_list.append(new_data)
    time.sleep(1)


if __name__ == "__main__":
    start_time = time.time()
    t_list = []
    for i in range(len(lists)):
        # 创建一个线程对象，并将其放入列表
        t = threading.Thread(target=work)
        t_list.append(t)
        t.start()
    for t in t_list:
        t.join()
    print("old lists:", lists)
    print("new lists", new_list)
    print("时间间隔为%s" %(time.time() - start_time))
