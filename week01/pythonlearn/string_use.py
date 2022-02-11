# coding=utf-8

"""
    测试对in和not in的用法
    内置函数id()，返回结果是变量的内存地址
"""

str = "张翔宇"
result = "翔宇" in str
print(result)
print(id(result))

result = "翔宇" not in str
print(result)
print(id(result))

"""
    测试对内置函数max、min的使用
"""

s = "zhangxiangyu"
# 查看字符串中哪个成员最大
print(max(s))
# 哪个成员最小
print(min(s))


"""
    测试一下字符串的拼接
"""

str1 = "张翔宇."
str2 = "李姗珊"
print(str1 + str2)
str3 = str1 + str2
length = len(str3)
print(str3)
print(length)
print(type(length))