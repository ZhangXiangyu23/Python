# coding:utf-8

"""
    super关键字的使用
"""

class Parent(object):
    def __init__(self):
        print("I am parent")


class Child(Parent):
    def __init__(self):
        print("I am child")
        super().__init__()  # 继承

if __name__ == "__main__":
    c = Child()