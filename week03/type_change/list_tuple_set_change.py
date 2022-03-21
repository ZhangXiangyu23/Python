# coding:utf-8

"""
    列表、元组、集合之间的转化
"""

info_list = ["zxy", "lss", "123"]
info_tuple = (1, 2, 3)
info_set = {4, 5, 6}
print(type(info_list))
print(type(info_tuple))
print(type(info_set))

# 将元组、集合转成列表
print(list(info_set))
print(list(info_tuple))
print(type(list(info_set)))
print(type(list(info_tuple)))

# is比较的内存地址
# 将列表、集合转成元组
print(tuple(info_set))
print(tuple(info_list))

# 将元组、列表转成集合
print(set(info_list))
print(set(info_tuple))

# str可以将列表、元组、集合转化成字符串类型
print(str(info_list))  # '['zxy', 'lss', '123']'
print(type(str(info_list)))
print(str(info_tuple))  # '(1, 2, 3)'
print(type(str(info_tuple)))
print(str(info_set))  # '{4, 5, 6}'
print(type(str(info_set)))

# str函数可以将列表、元组、集合转化成字符串类型，但是这个过程不可逆
# 再次使用list、tuple、set函数,无法将其转化回来，转化回来的就改变了
print(list(str(info_list)))
print(tuple(str(info_tuple)))
print(set(str(info_set)))