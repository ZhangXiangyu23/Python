# coding:utf-8

"""
    字典中copy函数的使用
"""

girl = {
    "name": "lss",
    "age": 22,
    "sex": "女"
}

new_girl = girl.copy()
print(new_girl)
# copy之后，两个字典的地址不一样！！！
print("旧字典的地址", id(girl))
print("新字典的地址", id(new_girl))