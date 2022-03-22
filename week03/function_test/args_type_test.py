# coding:utf-8

"""
    给参数搞个类型
"""

def add(num1:int, num2:int = 3):
    print(num1 + num2)


# 传入两个整数
add(1, 2)
# 传入两个字符串，不会报错，会将两个字符串进行拼接
# 函数定义里面，书写类型，是起到提示作用
# 即使不按要求进行传参，也不会报错的
add("hello", "zxy")

