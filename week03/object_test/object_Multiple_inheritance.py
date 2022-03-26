# coding:utf-8

"""
    多重继承，继承好几个父类
    (取百家之长！！！！)
"""

# 父类1
class Tool(object):
    def work(self):
        return "tool work"

    def car(self):
        return "car will run"

# 父类2
class Food(object):
    def work(self):
        return "food work"
    def cake(self):
        return "cake will eat"

# 子类  (多重继承)
class test(Tool, Food):
    pass

if __name__ == "__main__":
    t = test()
    print(t.car())
    print(t.cake())
    # 如果执行的函数，在两个继承的父类中都有的话，会优先执行第一个继承的父类
    print(t.work())  # tool work

    # 打印继承链
    print(test.__mro__)
