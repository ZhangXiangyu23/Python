# coding:utf-8

"""
    finally是try except finally中最后执行的
    而且是强制执行
"""


def test1():
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(e)
    finally:
        return "finally"

# 调用
result = test1()
print(result)


"""
    当except中有return时
    即使是有return,也会先执行finally中的内容，然后再结束
    因为finally是强制执行的
"""

def test2():
    try:
        1 / 0
    except Exception as e:
        print("123")
        return e
    finally:
        print("程序出错!")

# 调用
print("-" * 100)
result = test2()
print(result)


"""
    当try中有return时
    先执行finally中的内容，最后执行return
"""

def test3():
    try:
        print("999")
        return "666"
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("finally")


# 调用
print("*" * 100)
result = test3()
print(result)

"""
    finally具有必然触发性
"""