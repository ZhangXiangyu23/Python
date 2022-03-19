# coding:utf-8

"""
    集合的增删改
"""

# 添加
books = ["python", "c++", "c#", "java", "python"]
print(books)
# 将列表元素依次添加到空集合中
a_set = set()  # 定义一个空集合
# 不能这样定义空集合，这样python解释器会把它识别成空字典的
# a_set = {}
print(a_set)
print(type(a_set))

# 添加
# n = 0
# while n < len(books):
#     a_set.add(books[n])
#     n += 1

# 挨个添加，这有个知识点是：python中索引从前往后数是，下标从0数起
# 从后往前数是，下标从-1数起
a_set.add(books[0])
a_set.add(books[1])
a_set.add(books[2])
a_set.add(books[3])
a_set.add(books[4])
print(a_set)

"""
    update函数的使用，参数是迭代类型（比如:列表、元组、字符串、字典）
    将迭代数据类型种的各个元素，添加到集合中
"""

empty_set = set()
print(empty_set)
print(type(empty_set))
# 添加元组
info_tuple = ("zxy", "lss")
empty_set.update(info_tuple)
print(empty_set)

# 添加字符串，会将字符串看作是一个一个字母的迭代类型，一个一个字母的添加进去
empty_set.update("zxy")
print(empty_set)  # 'zxy', 'lss', 'z', 'x', 'y'

"""
    remove函数
    参数：必须是集合中的元素，不能是索引（集合没有索引这个概念）
    如果集合中找不到这个要删除的元素，那么会报错的
"""

print(empty_set)
# 删除
empty_set.remove("y")
print("删除之后", empty_set)
# 删除集合中没有的元素时，会报错的
# empty_set.remove("lxy")

"""
    clear函数：清空集合中的所有元素
"""
print("-------------------")
print("清空之前", empty_set)
empty_set.clear()
print("清空之后", empty_set)
# 由此得出了：集合如果为空时，显示set();集合不为空时，是{相应的元素}

# del的使用，从内存中删除这个集合，不支持索引删除（集合中没有索引这个概念）
del empty_set
print(empty_set)

