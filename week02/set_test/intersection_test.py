# coding:utf-8

"""
    intersection函数，寻找本集合与其他集合的交集
"""

a = ["python", "c++", "java"]
b = ["math", "python", "c++"]
c = ["c", "python", "php"]

a_set = set(a)
b_set = set(b)
c_set = set(c)

print("公共的书籍", a_set.intersection(b_set, c_set))