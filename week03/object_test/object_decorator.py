# coding:utf-8

"""
    装饰器的使用
    装饰器就相当于一个传入参数是函数的函数
"""

def check_str(fun):
    print(fun)
    def inter(*args, **kwargs):
        print(args, kwargs)
        result = fun(*args, **kwargs)
        if result == "ok":
            print(f"result is {result}")
        else:
            print(f"result is failed {result}")
    return inter

@check_str
def test(data):
    return data

test(data="lss")