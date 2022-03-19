# coding:utf-8

"""
    集合类型的定义
"""

a_set = set({})
print(a_set)
print(type(a_set))

b_set = set([1, 2, 3])
print(b_set)
print(type(b_set))

"""
    集合类型{}中，应该传入的是不可改变的类型，比如:元组、字符串
    如果传入了可变类型，比如：列表、字典   会报错的
"""

# c_set = {[1, 2, 5]}
# c_set = {{"name": "zxy", "age": 15}}
c_set = {(5, 2, 0)}
print(c_set)

# 集合是无序的
d_set = {"zxy", "123", "789"}
print(d_set)

# 集合是不允许出现重复值的
e_set = {"python", "flask", "python", "c++"}
print(e_set)


# 使用的小tip: 利用集合里面不出现重复值，使用集合帮助列表去重
info_list = [1, 2, 3, 2, 3, 5]
print(info_list)
print("去重之后", set(info_list))