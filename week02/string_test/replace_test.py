# coding:utf-8

"""
    replace函数有三个参数
    第一个参数表示:被替换的字符
    第二个参数表示:替换字符
    第三个参数如果不写的话，表示替换字符串中所有存在的第一个参数为第二个参数
    如果写的话，就只替换前N个字符（N的数值=第三个参数）
"""

info_01 = "I am zxy"
print(info_01)
print(info_01.replace("zxy", "lss"))


info_02 = "zxy zxy zxy"
print(info_02)
print(info_02.replace("zxy", "lss", 1))