# coding:utf-8

history_books = []
code_books = []

new_history_books = ("中国历史", "日本历史", "韩国历史")
new_code_books = ("C++", "java", "python")

history_books.extend(new_history_books)
print(history_books)
code_books.extend(new_code_books)
print(code_books)

# 将历史书合并到编程书里面，然后清除历史书架
code_books.extend(history_books)
print(code_books)
print(type(code_books))
print(type(new_code_books))
# del history_books
# print(history_books)


# extend函数的参数类型有:列表、元组、字符串(拆开存储)、字典（只能存上key）
test = []
test.extend("123")
print(test)
test.extend({"dog": 1, "cat": 2})
print(test)
