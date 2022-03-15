# coding:utf-8

info = "I am %s, My age is %s!"
# print(info)

print(info % ("zxy", 21))
print(info % ("lss", 22))

# 格式化输出列表
book = ["Python", "Math", "English"]
print("我喜欢看的书有:%s" % book)

# 字典格式化输出
example_dict = {
    "a": "a",
    "b": "b",
    "c": "c"
}

print("我的字典是:%s" % example_dict)


"""
    2.使用内置函数format进行格式化
"""

info_01 = "我叫{}，今年{}岁"
print(info_01.format("zxy", 18))


"""
    3.使用f-string进行格式化
    注意点：
    (1)f
    (2){}里面必须是变量，变量应该提前定义好
    {}里面不能直接写上值
"""

name = "lss"
age = 15
info_02 = f"我叫{name},我的年龄是{age}"
print(info_02)

"""
    format格式化的话，既可以写值，也可以写变量，推荐使用format进行格式化
"""
print(info_02.format(name,age))
