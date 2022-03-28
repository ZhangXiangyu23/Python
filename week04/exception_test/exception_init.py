# coding:utf-8

"""
    使用通用异常
"""

def test(str_data):
    new_str = ""
    try:
        new_str = str_data.upper()
    except Exception as e:
        print("程序出错", e)
    return new_str


print(test("zxy"))
# print(test(1))
test(1)
"""
    使用具体的异常：ZeroDivisionError
    使用通用异常比较简单，但是如果知道具体异常的话使用具体的异常更好    
"""

def test1():
    try:
        1/0
    except ZeroDivisionError as e:
        print("程序出错", e)

# 调用函数
test1()


"""
    捕获多个异常
    将多个异常名放到一个元组中
"""

def test2():
    try:
        print(name)
    except (ZeroDivisionError, NameError) as e:
        print("程序出错", e)

# 调用
test2()



