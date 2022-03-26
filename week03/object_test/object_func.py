# coding:utf-8

"""
    类的高级内置函数（两边有__）
"""

# __str__内置函数，功能是：当打印这个实例化对象时，返回return的内容（对类的介绍）
# __getattr__内置函数，功能是：当实例化对象调用不存在的属性时，使用这个内置函数会“友好”的提示；而不是报错

class Test(object):
    # 对类的介绍
    def __str__(self):
        return "this is a test class"
    # pass

    def __getattr__(self, key):
        print(f"这个属性{key}不存在")

    def __setattr__(self, key, value):
        # 将属性值key-value设置进内置的字典中
        if key not in self.__dict__:
            self.__dict__[key] = value
        print(self.__dict__)

    # __call__内置函数，之后的实例化对象可以直接像函数一样执行，直接对象名(参数)
    # 不用先.__call__函数，再传参数
    def __call__(self, *args, **kwargs):
        print("__call__内置函数执行")
        print(args)




# 实例化对象
t = Test()
# 直接打印实例化对象
# print(t)  # <__main__.Test object at 0x000001484D4CA2E0>
# 使用了内置函数__str__，就会返回对类的介绍
print(t)

# 打印类中不存在的属性，会报错
# print(t.a)  # AttributeError: 'Test' object has no attribute 'a'
t.a


"""
    setattr内置函数
    将属性和对应的值设置进入“类字典”中
"""
# 直接通过实例化对象设置类的属性
# t.name = "zxy"
# print(t.name)
#
# # 实例化
# k = Test()
# print(k.name)


print("-" * 100)
# 将name属性加入
t.name = "lxy"
print(t.name)

"""
    __call__内置函数
"""
# 不用.call函数，直接传参就能执行
t("520")