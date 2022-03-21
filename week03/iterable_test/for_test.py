# coding:utf-8

"""
    for循环的练习
"""

# 列表使用for循环
books = ["python", "c++", "java"]
for item in books:
    print(item)

# 字符串使用for循环
for i in "python":
    print(i)

# 元组使用for循环
info = ("zxy", "lss", "kakaka")
for name in info:
    if name == "zxy":
        print(name, "yyds")
    else:
        print("hello,{}".format(name))
    print("------------")

print("*****************")

# 对字典使用for循环
dict ={
    "zxy": 100,
    "lss": 99,
    "lxy": 66
}

for i in dict:
    print(i, dict[i])