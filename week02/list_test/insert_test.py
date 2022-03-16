# coding:utf-8

"""
    insert函数的使用，在指定位置，插入指定的元素
"""

num_list = ["dog", "cat", "tiger"]
print(num_list)
num_list.insert(1, "sweet")
print(num_list)
# 超出范围的话，就相当于append函数一样，将其放在列表末尾
num_list.insert(8, "zxy")
print(num_list)