# coding:utf-8

"""
    union函数:算集合的并集
"""

info_01 = ["python", "c++", "java"]
info_02 = ["c++", "python", "math"]
info_03 = ["c#", "php", "python"]

# 将列表转化成集合
info_01_set = set(info_01)
info_02_set = set(info_02)
info_03_set = set(info_03)

# 交集
print("交集是", info_01_set.intersection(info_02_set, info_03_set))
# 两个集合的差集
print("集合1和集合2的差集", info_01_set.difference(info_02_set))
# 三个集合的并集
print("三个集合的并集", info_01_set.union(info_02_set, info_03_set))

# 对于算一个集合的并集，其实union的参数使用列表也可以（只要是迭代类型就行）
print(info_01_set.union(info_02, info_03))

# 使用元组进行测试，union函数
tuple_01 = ("zxy", "lss", "james")
tuple_02 = ("zxy", "lss", "123")
tuple_03 = ("456", "789")

tuple_01_set = set(tuple_01)
print("并集是", tuple_01_set.union(tuple_02, tuple_03))
# 所以参数可以是所有的迭代类型