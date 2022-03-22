# coding:utf-8


"""
    全局变量和局部变量
"""
# 全局变量，在函数体内可以读取，但是不能修改
a = 5

def test_1():
    a = 9
    print("函数体内", a)

test_1()
print("函数体外", a)
# 说明在函数体内使用全局变量，只是读取，没有进行改变

# 局部变量只能在局部使用
# 例子如下

def test_2():
    name = "zxy"
    print(name)  # 内部能够使用

test_2()
# 在函数体外，使用函数体内定义局部变量，会报错的！！
# print(name)  # NameError: name 'name' is not defined

# global关键字的使用。 使用global在函数体内可以对全局变量进行修改
age = 99
print("修改之前", age)
def test_3():
    global age
    age = 55
    print("函数体内", age)

test_3()
print("修改之后", age)
# 通过global对全局变量做了修改

# 如果需要在函数体内对字典、列表进行修改，不需要使用global函数
# 元组不能修改
# 例子如下
books = ["python", "c++", "java"]
print("修改之前", books)
def test_4():
    books.append("c")
test_4()  # 调用
print("修改之后", books)

# 测试字典
info = {
    "zxy": 100,
    "lss": 99
}
print("修改之前", info)
def test_5():
    info["kaka"] = 60
# 得保证调用
test_5()
print("修改之后", info)

# 试一下元组
# 元组不能修改
# print(dir(info_01))
# global内置函数，对字符串类型、数字类型、None、bool类型管用

