# coding:utf-8

"""
    两层for循环
"""

num_01 = [1, 2, 3]
num_02 = [4, 5, 6]

for i in num_01:
    for j in num_02:
        print(i+j)

# for循环写一个九九乘法表
num_03 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_04 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in num_03:
    for j in num_04:
        if j <= i:
            print("{}*{}={}".format(i, j, i*j), end="   ")
    print()



