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

"""
    items函数的使用
    对字典使用items函数，会返回一个伪列表
    伪列表中的元素是一个元组，元组中第一个元素是key,第二个元素是value
"""
print(dict.items())
print(type(dict.items()))

# 使用items函数
for key, value in dict.items():
    print(key, value)


# range函数的使用
# range函数，有三个参数
# 第一个参数是start，第二个参数是end，第三个参数是跳步（每隔几个）
# l = range(5)  # 相当于生成0~4（左闭右开）
# print(l)
# print("类型为", type(l))
#
# # 遍历
# for i in l:
#     print(i)
# else:
#     print("for循环结束了！！！！")