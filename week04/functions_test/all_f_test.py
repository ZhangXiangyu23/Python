# coding:utf-8

# abs函数
num = -8
print(abs(num))

# all函数
# 列表中全为True时，返回True;其余情况返回False
print(all(["zxy", None]))

# 枚举函数enumerate
# 可以将索引显示出来
books = ["c++", "java", "python"]
for index, item in enumerate(books):
    print(index, item)


# help函数
# 对一些数据类型的介绍
print(help(list))

print(dir(list))

# any函数
# 只要有True就返回True
info = ["123", None, False]
print(any(info))