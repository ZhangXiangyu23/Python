# coding:utf-8

"""
    自定义异常以及raise关键字的使用
    有些时候需要用“异常”来警示别人（自定义爆红来警告别人）
"""

def test1(num):
    if num == 100:
        raise TypeError("数值不能是100")
    else:
        return num

# 调用
# 自定义爆红！！！
# result = test1(100)
# print(result)

# 捕获自定义异常
def test2():
    try:
        test1(100)
    except Exception as e:
        print("异常为", e)

# 调用
test2()

"""
    自定义异常类
"""

# 让这个异常类继承自父类（Exception）
class strlimitException(Exception):
    def __init__(self, message):
        self.message = message


def test3(name):
    if name == "zxy":
        raise strlimitException("不能书写zxy")
    else:
        return name

# 调用
# test3("zxy")

# 捕获异常
print("-" * 100)
try:
    test3("zxy")
except strlimitException as e:
    print(e)

"""
    自定义数字限制异常类，使用raise关键字自定义异常报错话语，最后捕获该异常
"""

class numlimitException(Exception):
    def __init__(self, message):
        self.message = message

def test4(num):
    if num > 100:
        raise numlimitException("数字不能超过100")
    else:
        return num

# 测试异常
print("&" * 100)
result = test4(100)
print(result)

# test4(120)

# 捕获异常
print("$" * 100)
try:
    test4(120)
except numlimitException as e:
    print(e)
