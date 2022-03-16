# coding:utf-8

num_list = [5, 6, 2, 0, -5, 3, 9]
print(f"排序前{num_list}")
# 默认升序排列
num_list.sort()
print(f"排序之后{num_list}")

# 降序排序
num_list.sort(reverse=True)
print(num_list)

# 再进行降序
# 已经是降序排列了，所以就是会保持原状
num_list.sort(reverse=True)
print(num_list)
