# coding:utf-8

# 小括号中只有一个元素时，要表示元组，得在后面多加一个逗号才行
# 否则就会认为是单个元素本身的类型
tuple_test = ('zxy',)
print(tuple_test)
print(type(tuple_test))

tuple_1 = tuple()
print(type(tuple_1))
# 元组不为空，返回结构True
print(bool((1, )))
print(bool(()))
tuple_2 = (1, "zxy", 2, True)
print(len(tuple_2))


tuple_3 = (1, 2, 3)
# 内置函数max和min在元组中的使用
print(max(tuple_3))
print(min(tuple_3))
