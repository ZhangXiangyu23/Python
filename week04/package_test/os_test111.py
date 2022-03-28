# coding:utf-8

import os

current = os.getcwd()
print(current)

# 创建一个文件夹
new_path = "%s/test1" % current
# os.makedirs(new_path)

# 展示当前路径下的内容
data = os.listdir(current)
print(data)

# 删除空文件夹
# os.rmdir("test1")

# 创建一个文件（顺带创建一个文件夹）
path = "%s/zxy/test.py" % current
# os.makedirs(path)

# 递归删除全部的文件夹
# os.removedirs(path)

# 给文件改名
# os.renames("os_test.py", "os_test111.py")

# 判断路径是否存在
print(os.path.exists(os.getcwd()))
print(os.path.exists("%s/123" % current))

# join
l = os.path.join(current, "lss", "666")
print(l)

# split函数
print(l.split(current))

# isfile:判断是否是文件
print(os.path.isfile(current))

# 判断是否是文件夹
print(os.path.isdir(current))

# 判断路径是否为绝对路径
print(os.path.isabs(current))
print(os.path.isabs(".test"))