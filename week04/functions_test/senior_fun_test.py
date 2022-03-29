# coding:utf-8

"""
    测试几个返回类型是迭代器的高级函数
"""

# 导入reduce模块
from functools import reduce

books = ["c#", "c++", "java"]

# x相当于是books中的每个元素
# filter函数
result = filter(lambda x: "c" in x, books)
print(list(result))

# reduce函数
r = reduce(lambda x, y: x + y, [0, 1, 2])
print(r)

# 再次测试reduce函数
# lambda相当于函数的标记
# x代表books中每个元素
# y代表返回值， y:x+y表示返回值
zxy = reduce(lambda x, y: x + y, books)
print(zxy)


def filter_func(item):
    if "c" in item:
        return True

l = filter(filter_func, books)
print(list(l))

# map函数
c = map(filter_func, books)
print(list(c))
