# coding:utf-8

"""
    成员运算符in和not in在字典中的使用
"""

books = {
    "python": 20,
    "C++": 18,
    "Java": 15
}

# 通过key来判断的
print("python" in books)
print("1" in books)
print("1" not in books)

# 使用get函数进行判断
print(bool(books.get("C++")))
# 但是如果字典中key对应的值正好是0、False、None时，使用get函数进行判断是否存在，就不合适！！！
