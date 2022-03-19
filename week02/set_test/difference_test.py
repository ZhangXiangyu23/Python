# coding:utf-8

"""
    difference函数，两个集合作差集
    就是找出和另一个集合不一样的元素，然后将其包装成一个集合返回
"""

books_a = ["python", "c++", "java"]
books_b = ["python", "c#", "c"]

books_a_set = set(books_a)
books_b_set = set(books_b)
print(books_a_set)
print(books_b_set)

print("两个集合的差集是", books_a_set.difference(books_b_set))  # "c++", "java"
