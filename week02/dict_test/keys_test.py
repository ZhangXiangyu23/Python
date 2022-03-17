# coding:utf-8

"""
    keys函数
    字典的内置函数：keys函数,没有参数
    使用keys函数可以返回一个伪列表（格式是：dict_keys([各个key值])），不具备列表的全部功能
    需要通过list()将伪列表转化成真正的列表
"""

user = {
    "name": "zxy",
    "age": 20,
    "girlfriend": "lss"
}

user_title = user.keys()
print(user_title)
# 伪列表不具备列表的特性
# print(user_title[1])
# user_title.append("123")

# 将伪列表转化成列表
real_list = list(user_title)
print(real_list)
print(real_list[1])
real_list.append("love")
print(real_list)
