# coding:utf-8

"""
    values函数，将字典中的全部值取出来，放到一个伪列表中
    非常类似于keys函数
"""

user = {
    "name": "zxy",
    "age": 18,
    "love": "lss"
}
print(user)
print("伪列表是",user.values())
values_list = list(user.values())
print("字典中的值的列表", values_list)
values_list.append("123")
print(values_list)