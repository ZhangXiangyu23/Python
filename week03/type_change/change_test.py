# coding:utf-8

"""
    字符串类型和数字类型（整形、浮点型）之间的相互转换
"""

# 数字类型转化成字符串类型
num_01 = 10
num_02 = 3.14

str_01 = str(num_01)
str_02 = str(num_02)
print(str_01, str_02)
print("类型分别是", type(str_01), type(str_02))

# 测试0和负数
num_zero = 0
num_fu = -2

str_03 = str(num_zero)
str_04 = str(num_fu)

print(str_03, str_04)
print(type(str_03), type(str_04))

# 将字符串类型转化成数字类型
str_05 = "123"
str_06 = "3.14"

int_01 = int(str_05)
float_01 = float(str_06)

print(int_01, float_01)
print("他们的类型分别是", type(int_01), type(float_01))
