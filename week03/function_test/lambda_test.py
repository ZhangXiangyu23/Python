# coding:utf-8

"""
    匿名函数
"""

# 匿名函数， :后面相当于一个函数中的return返回值
f = lambda : 520
# 像调用普通函数一样，调用
result = f()
print(result)

# lambda相当于一个函数的标记，后面可以写参数。冒号后面可以写值，相当于return
# 冒号后面也可以写一些表达式
s = lambda a, b : a + b
print(s(1, 2))
x = lambda a, b : a > b
print(x(5, 2))

# 使用lambda进行排序
user = [
    {"name": "zxy"},
    {"name": "lss"},
    {"name": "asan"}
]
# 这里的x相当于user中每个字典元素，冒号后面的x["name"]是取name值；按name对应的值进行排序
user.sort(key= lambda x : x["name"])
print(user)