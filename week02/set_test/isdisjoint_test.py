# coding:utf-8

""""
    isdisjoint函数
    如果存在和本集合相同的元素，则返回False
    如果存在和本集合不同的元素，则返回True
"""

not_allow = {"喝酒", "抽烟", "赌博"}
print(type(not_allow))
one_candidate = {"python", "c++"}
two_candidate = {"喝酒", "java", "666"}
three_candidate = {"抽烟", "456"}

print(not_allow.isdisjoint(one_candidate))  # True
print(not_allow.isdisjoint(two_candidate))  # False
print(not_allow.isdisjoint(three_candidate))  # False
