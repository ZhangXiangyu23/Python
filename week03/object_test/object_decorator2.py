# coding:utf-8

"""
    常见的装饰器
"""

class Test(object):
    def __init__(self, a):
        self.a = a

    def run(self):
        print("run")
        self.jump()
        self.sleep()

    @classmethod
    def jump(cls):
        print("jump")

    @staticmethod
    def sleep():
        print("sleep")

    @property
    def sing(self):
        print("sing")





# 实例化对象
t = Test("a")
t.run()

# 不去实例化对象，直接去调用
# 因为没有实例化对象，就直接去调用，所以会报错   TypeError: run() missing 1 required positional argument: 'self'
# 显示没有传入self参数，self参数是实例化对象之后才会传入的
# Test.run()


# 如果不实例化对象，就直接调用类函数，得使用@classmethod装饰器
Test.jump()
# 在类内部，可以使用self调用@classmethod装饰器的函数；但是在@classmethod装饰器的函数内部，无法调用self函数


"""
    使用@staticmethod装饰器，不需要在类函数中加参数self,也不需要加参数cls
    就可以直接不实例化，就直接调用
"""
# 不实例化对象进行调用，就是直接使用类名进行调用
Test.sleep()
# 实例化对象进行调用@staticmethod装饰器函数
t.sleep()

# 在正常的函数内可以使用self来调用@classmethod函数和@staticmethod函数
# @staticmethod函数不能调用上述两种函数
print("-" * 100)
t.run()

"""
    @property装饰器 
    类函数中加上这个装饰器，调用这个类函数的时候，不需要使用()
"""

class Test2(object):
    def __init__(self, name):
        self.__name = name

    @property
    def code(self):
        return self.__name

    @code.setter
    def code(self, value):
        self.__name = value


# 不使用()就直接调用@property装饰器的类函数
print("%" * 100)
zxy = Test2("123")
print(zxy.code)

# 通过@code.setter装饰器修改属性
# 通过@code.setter装饰器修改私有变量
zxy.name = "999"
# 通过@property装饰器，直接像调用属性一样调用类函数，不用()
print(zxy.name)