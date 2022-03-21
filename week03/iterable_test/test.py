# coding:utf-8

"""
    使用for循环和while循环来打印九九乘法表
"""

# 使用for循环
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(i, j, i * j), end="  ")
    print("")



print("-" * 100)
# 使用while循环
i = 1
j = 1

while i <= 9:
    while j <= 9:
        print("{}*{}={}".format(i, j, i * j), end="  ")
        j += 1
        if j > i:
            j = 1  # 归1
            break
    i += 1
    print("")