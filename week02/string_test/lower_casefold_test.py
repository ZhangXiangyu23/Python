# coding:utf-8


"""
    将字符串中的大写字母全部转化成小写字母，有两种方法：lower和casefold
    区别：
    lower:是将英文的大写全部转化成小写
    casefold:可以将多种语言的大写转化成小写（不局限于英文）
"""

info_01 = "I Am Zxy"
print("lower:" + info_01.lower())
print("casefold:" + info_01.casefold())

# 对于空字符串
info_02 = "    "
print("." + info_02 + ".")
print("lower:" + info_02.lower())
print("casefold:" + info_02.casefold())
