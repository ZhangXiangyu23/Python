# coding:utf-8

"""
    get函数:通过传入key,
    如果传入参数key在字典中存在，那么返回key对应的value
    如果传入的参数key在字典中不存在，那么返回None

    使用[]形式去取key对应的value，如果key在字典中不存在的话，会报错
"""

user = {
    "name": "zxy",
    "password": "123456",
    "age": 15,
    "123": None
}

print(user.values())

# 模拟一下values函数
info = []
info.append(user.get("name"))
info.append(user.get("password"))
info.append(user.get("age"))
info.append(user.get("123", "456"))
print(info)
# get函数，要找的key如果在字典中不存在，那么返回值为None
# info.append(user.get("123"))
# print(info)
# # 使用[]找值，key如果不存在，就会报错的！
# # info.append(user["456"])
# print(info)
#
# print("--------------------------")
# books = {
#     "python": 10,
#     "c++": 15,
#     "java": 20
# }
#
# # 使用get的第二个参数
# # 当传入的参数key在字典中没有时,会返回默认值None
# # 如果第二个参数有值时，会返回第二个参数的值
# r = books.get("math", "123")
# print(r)