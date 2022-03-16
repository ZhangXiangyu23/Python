# coding:utf-8

"""
    1.变量赋值之后，其实内存地址是一样的，两个变量共用一个内存地址
    所以数据是共享的
    2.而使用copy函数，两个变量的内存地址是不同的，所以是不共享的
    3.浅拷贝，就是对于深层列表的改变，两个变量是共享的，一个改变，另一个也会改变
    （第一层列表不共享、深层列表共享）
    4.深拷贝，对于深层列表的改变，两个变量不共享。一个改变不影响另一个
    （第一层列表不共享，深层列表也不共享）
"""

old_num_list = [5, 3, 6, -5, 0]
print(old_num_list)
new_num_list = old_num_list
print(new_num_list)
print(f"旧地址:{id(old_num_list)}")
print(f"新地址:{id(new_num_list)}")

# copy的使用
old_info = ["lss", "zxy"]
print(old_info)
new_info = old_info.copy()
print(new_info)
old_info.append("123")
print(new_info)
print(old_info)

# 两个的地址
# 两个的地址不一致
print("老地址是:%s" % id(old_info))
print("新地址是:%s" % id(new_info))