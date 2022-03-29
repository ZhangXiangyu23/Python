# coding:utf-8

"""
    random模块的使用
"""

import random

gifts = ["iphone", "tv", "ipad", "mac"]

# random中的choice函数，选一个传入参数（迭代类型的）中的元素返回
def choice():
    gift = random.choice(gifts)
    print("抽到了%s" % gift)

#
def new_choice():
    count = random.randrange(0, 100, 1)
    print(count)
    if 0 <= count <= 50:
        print("你中了一个mac!")
    elif 50 < count <= 60:
        print("你中了一个iPhone!")
    elif 60 < count <= 80:
        print("你中了一个tv!")
    elif count > 80:
        print("你中了ipad!")

if __name__ == "__main__":
    # choice()
    new_choice()