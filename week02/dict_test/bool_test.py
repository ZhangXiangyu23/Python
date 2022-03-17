# coding:utf-8

"""
    bool值表
    not进行取反
"""

# int类型
a_1 = 1
a_2 = 0
print(bool(a_1))  # True
print(bool(a_2))  # False

# float
b_1 = 1.0
b_2 = 0.0
print(bool(b_1))
print(bool(b_2))

# 字符串，长度为0时为False,长度不为0时为True
c_1 = "zxy"
c_2 = ""
print(bool(c_1))
print(bool(c_2))

# 列表，长度为0是为False,长度不为0时为True
d_1 = [1, 2, 3]
d_2 = []
print(bool(d_1))
print(bool(d_2))

# 元组
e_1 = ("zxy", "lss")
e_2 =()
print(bool(e_1))
print(bool(e_2))

# 字典
f_1 ={
    "name": "zxy",
    "age": 18
}
f_2 = {}
print(bool(f_1))
print(bool(f_2))

# 空类型None
print(bool(None))
print(bool(not None))