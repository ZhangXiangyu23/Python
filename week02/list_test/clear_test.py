# coding:utf-8

"""
    clear函数：将列表中的元素全部清空
"""

num_list = [5, 3, 6, 9, -8]
print(num_list)
print(len(num_list))
num_list.clear()
print(num_list)
print(len(num_list))

# 在写程序的过程中，清空已经定义的列表，然后再使用，效率要高于：新定义一个列表
# 因为新定义一个列表，需要重新申请一片内存空间。而clear一个已经定义好的列表，效率更高，只是将原来的元素请出去
# 而新定义列表的话，需要重新盖房子！