# coding:utf-8

"""
    1.列表，元组，字符串都有索引这个概念；可以通过索引来修改相应的值
    2.字典中没有索引的概念，可以将key比作是字典的索引
    3.对字典进行添加的话，直接是:字典名["新key"] = 值
    4.对字典进行修改的话，可以是:字典名["旧key"] = 值
"""

user = {
    "name": "zxy",
    "age": 20
}

print("原来的字典是", user)

# 进行添加操作
user["height"] = 180
print("添加之后", user)

# 进行修改操作
user["name"] = "lss"
print("修改之后", user)


print("---------------------------")
"""
    字典内置函数update:通过将新的字典作为参数传入
    如果新字典中的key和旧字典中的key一样，那么新字典中的值将会替代旧字典中的值
    如果旧字典没有新字典中的key,那么直接抄上新字典中的key-value
"""

old_book = {
    "name": "python",
    "price": 15
}
new_book = {
    "name": "C++",
    "price": 18,
    "age": 5
}
print("更新之前",old_book)
old_book.update(new_book)
print("更新之后", old_book)

print("----------------------")
"""
    setdefault函数:参数是一个键值对
    如果原来字典中有这个key,那么不改变原字典中键值对，返回值为原字典中key对应的值
    如果原来字典中没有这个key,那么将这个新的键值对存入字典中
"""

info = {
    "name": "lss",
    "age": 18
}

# 原来字典中有这个key, setdefault默认取值功能
result = info.setdefault("name", "zxy")
print(result)  # lss

# 原来字典中没有这个key，setdefault默认存储功能
result = info.setdefault("weight", 50)
print(result)
print(info)