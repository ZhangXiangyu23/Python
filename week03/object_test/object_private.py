# coding:utf-8

"""
    私有属性和私有方法
    私有属性和私有方法只能在类的内部进行调用
    类外部的实例化对象无法进行调用私有方法和私有属性
    私有属性和私有方法就是在普通名称前面加上__
"""

class Cat(object):
    __cat_type = "cat"
    def __init__(self, name, age=None):
        self.name = name
        self.__age = age

    def run(self):
        result = self.__run()
        print(result)

    def __run(self):
        return f"{self.__cat_type}小猫{self.name}在奔跑, {self.__age}"

    def jump(self):
        result = self.__jump()
        print(result)

    def __jump(self):
        return f"{self.__cat_type}小猫{self.name}在跳跃, {self.__age}"


# 实例化对象
cat = Cat(name="咪咪")
cat.run()
cat.jump()

# 如果将数据类型看作是类的话，这种类型的变量就类似于实例化对象
# 我们可以使用dir内置函数来查看变量的内置函数，也可以使用dir内置函数来查看实例化对象的函数

info = ["python", "c++"]
print(dir(info))
# 查看实例化对象cat的内置函数
print(dir(cat))
# 强行调用类的私有方法，也是可以的
print("-" * 100)
print(cat._Cat__jump())
# pass用作占位符

"""
    测试使用私有属性
"""

zxy = Cat(name="zxy", age=18)
zxy.run()
zxy.jump()
# 强行调用私有属性
print(dir(zxy))
print(zxy._Cat__age)
print(zxy._Cat__cat_type)