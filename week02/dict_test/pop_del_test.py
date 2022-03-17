# coding:utf-8

"""
    pop函数以及del函数的使用
"""

project = {
    "mac": {"name": "mac", "price": 8000, "desc": "笔记本"},
    "ipad": {"name": "ipad", "price": 5000, "desc": "平板"},
    "iphone": {"name": "iphone", "price": 7000, "desc": "手机"}
}

print(project.keys())
# 小明买了一台iPhone
# pop函数中的参数是key值，如果存在，那么就将这个键值对删除掉，然后返回key对应的值
result = project.pop("iphone")
print("商店里面有", project.keys())
print("小明花了", result.get("price"))

print("-----------------------")
# r = project.pop("123")  # None
# print(r)
# clear的使用
print(project.keys())
print("清空商店中的商品")
project.clear()
print(project.keys())

# del删除这个字典
del project
print(project)