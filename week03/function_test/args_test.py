# coding:utf-8

"""
    参数的传递：1.必传参数 2.默认参数 3.可变参数（不确定参数）
"""


def add(a, b, c=3):
    return a + b + c;


# 第三个参数如果不传值，那么就使用默认参数
print(add(1, 2))  # 6
# 如果第三个参数传了值，那么使用传入的值
print(add(1, 2, 8))  # 11


# 测试可变参数
# 传入参数，如果是“变量名=值”这种格式，那么就会把它们封装成字典
# 如果传入的是纯数值这种形式，那么就封装成元组
def test(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


test(1, 2, 3, 4, 5, name = "zxy", girlfriend = "lss")

# 测试函数2
def test2(*args, **kwargs):
    if len(args) >= 1:
        print(args)  # 打印元组
    if "name" in kwargs:
        print(kwargs["name"])
    else:
        print("no name")
    print(args, type(args))
    print(kwargs, type(kwargs))

test2(1, name="zxy")
# 如果直接将元组和字典传入的话
a_tuple = (1, 2, 3)
b_dict = {"name": "python"}
# 这样相当于将两个不是“变量=值”格式的，传入函数中
# test2函数，将它们两封装成一个元组
test2(a_tuple, b_dict)

print("-" * 100)  # 分割线
# 想要将元组和字典对应于args和kwargs传入，应该这样
test2(*a_tuple, **b_dict)

"""
    case1:三个参数分别是:必传参数、默认参数、*args
    (1)传值方式：只传值
    (2)赋值传递
"""

def test3(a, b, *args):
    print(a, b, args)

# 直接传值调用
s = ("zxy", "lss")
test3(1, 2, *s)
# 赋值传递
# 这种方法会报错
# test3(a=1, b=2, *s)


# 如何赋值调用  必传参数、默认参数、可变参数
# 定义函数的时候，应该按：可变参数、必传参数、默认参数的顺序
print("-" * 100)
def test4(*args, a, b):
    print(args, a, b)

# 传值调用，这样使用不行！！！
# test4(*s, 1, 2)
# 赋值传递
test4(*s, a=1, b=2)

"""
    case2:三个参数分别是:必传参数、默认参数、**kwargs
    直接传值传递和赋值传递两种方式都OK
"""

def test5(a, b, **kwargs):
    print(a, b, kwargs)

dict = {
    "name": "zxy",
    "age": 18
}
# 传值调用
print("@" * 100)
test5(1, 2, **dict)
# 赋值调用
test5(a=123,b=456, **dict)
test5(66, 456, **dict)
# 调用时，如果传参顺序和定义函数时参数顺序不一样，调用时就应该使用赋值传递。这样更明确一点！！！
# test5(**dict, 66, 77)  # 会报错的！

