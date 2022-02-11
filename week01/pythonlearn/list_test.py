# coding:utf-8

none_list = [None, None, None]
print(none_list)
print(len(none_list))
print(bool(none_list))
print([])
print(bool([]))


"""
    内置函数max和min在列表中的应用
"""
num_list = [1, 5, 10]
print(max(num_list))
print(min(num_list))
# 每次运行脚本，列表的地址都是不一样的！
# 因为每运行完一次，地址都会进行回收！
print(id(num_list))