# coding:utf-8

"""
    迭代器的使用
    用next函数去迭代：迭代器对象
    迭代器就是，不是一下子放入内存中；而是一个一个得放入
"""

# 创建迭代器，方法一
iter_obj = iter((1, 2, 3))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# 使用for循环来打印迭代器对象
for i in iter_obj:
    print(i)


# 创建迭代器，方法二
def make_iter():
    for i in range(10):
        # 添加到迭代器中
        yield i

# 创建迭代器
print("-" * 100)
iter_zxy = make_iter()
for i in iter_zxy:
    print(i)

# 创建迭代器，方法三
print("$" * 100)
lss_iter = (i for i in range(10))
for i in lss_iter:
    print(i)