# coding:utf-8

"""
    构造函数的使用
"""

class Person(object):
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def run(self):
        print("{}在奔跑".format(self.name))
    def sleep(self):
        print("{}在睡觉".format(self.name))


# 实例化zxy
zxy = Person(name="zxy", age=18)
zxy.name = "lss"
zxy.run()