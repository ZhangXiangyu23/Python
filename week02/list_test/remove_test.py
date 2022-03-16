# coding:utf-8

"""
    remove函数：在原先列表的基础上，将列表中的第一个存在的被指定的参数值删除掉
    列表是可以改变的，remove元素之后的列表还有原来的那个列表
    del 从内存中删除某个变量
"""

shops = ["cola", "sweet", "cola", "cake", "cake"]
print(f'超市中可乐的数量为{shops.count("cola")}')
print(f'超市中蛋糕的数量为{shops.count("cake")}')
print(f'超市中糖果的数量为{shops.count("sweet")}')

# 买一个cola
shops.remove("cola")
print(shops)

# del使用
del shops
print(shops)
