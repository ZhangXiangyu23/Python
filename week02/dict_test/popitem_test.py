# coding:utf-8

"""
    popitem函数，这个函数没有参数
    功能是:将字典末尾的键值对删除，返回值为一个元组（为了不让修改）
    元组的0索引为key,元组的1索引为value
"""

user_dict = {
    "name": "zxy",
    "age": 20,
    "height": 180
}

print("删除之前", user_dict)
user_dict.popitem()
print("删除之后", user_dict)

# 当字典为空时，使用popitem会报错
empty = {}
# empty.popitem()


