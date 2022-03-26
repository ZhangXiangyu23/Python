# coding:utf-8

"""
    父类和子类
"""

class Parent(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def talk(self):
        return f"{self.name} is talking"

    def check(self):
        if self.sex == "boy":
            return f"{self.name} is a boy"
        else:
            return f"{self.name} is a girl"

# 在括号中写上父类名
class childOne(Parent):
    def code(self):
        return f"{self.name} is coding"

class childTwo(Parent):
    def jump(self):
        return f"{self.name} is jumping"


# 实例化，然后调用
c1 = childOne("zxy", "boy")
print(c1.code())
print(c1.talk())
print(c1.check())

print("-" * 100)
c2 = childTwo("lss", "girl")
print(c2.check())