# coding:utf-8

books = ["python", "java"]
print(books)
books.append("c++")
print(books)

# append是否可以添加其他数据类型
num_01 = 1
num_02 = 3.14
name_tuple = ("zxy", "lss")
price_dict = {
    "apple": 12.5,
    "orange": 5
}

# append函数每次只能添加一个元素
# books.append(num_01, num_02, price_dict)
# print(books)

books.append(num_01)
books.append(num_02)
books.append(name_tuple)
books.append(price_dict)
print(books)
print(id(books))

# append也可以直接添加变量
books.append("flash")
print(books)

# 列表是否可以添加bool类型和空类型
books.append(None)
print(books)  # 可以添加空类型
print(id(books))
books.append(True)
print(books)
print(id(books))
books.append(False)
print(books)  # 可以添加bool类型

# append之后，列表的地址没有改变,也就是说列表是可变的！
print(id(books))