# coding:utf-8

"""
    使用自定义函数去模拟capitalize
"""
# info = "i am zxy"
# new_info = ""
# index = 0
# # 使用for循环，是因为字符串是不能改变的
# for i in info:
#     if index == 0:
#         i = i.upper()
#     new_info += i
#     index += 1
#
# print(new_info)


# 定义capitalize函数
def capitalize(info):
    new_info = ""
    index = 0
    for i in info:
        if index == 0:
            i = i.upper()
        new_info += i
        index += 1
    return new_info


books = "Math"
print(capitalize(books))


# 循环之后返回值
def return_5():
    for i in range(10):
        if i == 5:
            return i

print("结果是", return_5())

