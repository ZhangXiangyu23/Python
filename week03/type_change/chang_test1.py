# coding:utf-8

"""
    字符串和列表之间的转化
"""

# split函数中如果不写参数的话，默认使用空格进行分割
# 如果没有空格，那就不切割
str_01 = "abc"
print(str_01.split())

# 有空格的时候
str_02 = "a b c"
print(str_02.split(), type(str_02.split()))

# 第二个参数限制切割的次数
str_03 = "zxy|lss|123|456"
print(str_03.split("|"))
print(str_03.split("|", 1))


"""
    将列表转化成字符串类型
"""

# 将列表转化成字符串类型
books = ["python", "c++", "math"]
result = "%".join(books)
print("拼接之后", result)
print("拼接之后的类型", type(result))

# 列表中的成员是数字类型（整数型、浮点型）的都不行
# num_list = [1.1, 2, 3]
# print("#".join(num_list))

# 只有字符串类型的列表才能够通过join函数进行合并，其他类型不行
# 列表中的元素时元组时,会报错的
# TypeError: sequence item 0: expected str instance, tuple found
# info_01 = [(1, 2), (3, 4)]
# print("+".join(info_01))

# 列表中的元素时字典类型时,会报错的
# TypeError: sequence item 0: expected str instance, dict found
# info_02 = [{"zxy": 100}, {"lss": 99}]
# print("+".join(info_02))

# 列表中是None类型和布尔类型时
# TypeError: sequence item 0: expected str instance, NoneType found
# info_03 = [None, True]
# print("@".join(info_03))


"""
    给字符串中的字符进行排序
"""
info = "a e f c b d"
print(info)
info_list = info.split()
print(info_list)
info_list.sort()
print(info_list)
print(" ".join(info_list))

# sorted函数的使用
"""
    sorted内置函数的使用
    是将字符串中的字符挨个进行排序，最后返回一个列表
"""

# 将字符串排序后，返回一个列表
info_01 = "afedcx"
info_01_new = sorted(info_01)
print(info_01_new)
print("原来字符串", info_01)
print("之后字符串", "".join(info_01_new))
