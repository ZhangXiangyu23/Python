# coding:utf-8

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num_list)
print("最大索引是:%s" % (len(num_list)-1))


print(id(num_list))

# 切片的使用
# 全部输出，方法一
print(num_list[:])
print(id(num_list[:]))
# 全部输出，方法二
print(num_list[0:])
# 如果从后往前数数的话，那么最后一个元素的索引就是-1。
# 相当于从  左含默认的顺序0，右不含 最后一个索引（-1）
print(num_list[:-1])

# 切片之后的列表，和原来的列表不一样啊，地址发生了改变！
# 列表的反序
print("列表的反序:%s" % num_list[::-1])

# 列表反向切片(就是索引顺序从右往左数，依然是左含右不含)
print("列表的反序%s" % num_list[-3:-1])

# 间隔进行获取
print("步长为2的获取", num_list[0: 8: 2])
# 切片生成空列表
print("切片生成空列表", num_list[0:0])

# 通过索引来修改相应的值
print(num_list)
num_list[1] = "a"
print(num_list)
num_list[2:5] = "b", "c", "d"
print(num_list)

# index函数，返回一个值，就是返回参数在列表中的位置索引
print(num_list.index("a"))

# pop函数：通过索引将指定的索引所对应的值删除，返回值为被删除索引的元素值
pop_value = num_list.pop(1)
print("弹出的元素是",pop_value)
print("此时列表中的情况是:%s" % num_list,"列表长度为%s" % (len(num_list)))

# 通过del进行删除
del num_list[1]  # b将会被删除
print(num_list)

# 元组是不可以进行修改的
num_tuple = (1, 2, 3)
print(num_tuple)
# del num_tuple[0]
del num_tuple