# coding:utf-8

"""
    序列化和反序列化
    序列化的意思是：将python中的数据类型转化成json形式
"""
# 导入json模块
import json

a = 1
b = "zxy"
c = ["python", "c++", "java"]
d = ("zxy", "lss", "lxy")
e = {"name": "520"}

# 使用dumps函数进行序列化
a_json = json.dumps(a)
print(a_json, type(a_json))

b_json = json.dumps(b)
print(b_json, type(b_json))

c_json = json.dumps(c)
print(c_json, type(c_json))

# 元组序列化之后显示的是列表形式
d_json = json.dumps(d)
print(d_json, type(d_json))

# 字典类型比较特殊
e_json = json.dumps(e)
print(e_json, type(e_json))

"""
    使用loads函数反序列化
"""

# 元组
print("-" * 100)
print(d_json)
# 没变会来
print(json.loads(d_json))

# 字典
print("$" * 100)
print(e_json)
print(json.loads(e_json))


