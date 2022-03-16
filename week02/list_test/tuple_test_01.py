# coding:utf-8

name = ("zxy", "lxy", "lss")
name_add = name + name
name_c = name * 10

print(name)
print(name_add)
print(name_c)

print(len(name_c))

# 简写运算符的应用
# +=
age = (1, 2, 3)
print(age)
age += (5, )
print(age)
# *=
age *= 3
print(age)

# 成员运算符
book = ["python", "java", "c++"]
print("123" in book)
print("python" in book)