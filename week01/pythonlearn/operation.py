# coding:utf-8

a = 1
b = 2
c = 3
d = a + b + c
d += c
print(d)

# 测试运算
# 幂运算
c **= 3
print(c)

# 整除运算
c //= 2
print(c)

# 数据类型的乘法
# 字符串
str = 'zxy'
print(str * 3)

# 列表
list_01 = [1, 2, 3]
print(list_01 * 3)

# 元组
tuple_01 = ("zxy", "lss")
print(tuple_01 * 3)

# 字典不能使用乘法，因为key是唯一的，乘了之后就不唯一了
# TypeError: unsupported operand type(s) for *: 'dict' and 'int'
# dict_01 = {'name': 'zxy'}
# print(dict_01 * 3)

# 计算机中的进制转化
# 1GB = 1024MB
# 1MB = 1024KB
# 1KB = 1024B
gb = 1
b = 1 * 1024 * 1024 * 1024
print(b)
