# coding:utf-8

"""
    while循环的使用
"""

num = 0
while num < 5:
    print(num, end="")
    num += 1

# 计算1~100的和
n = 0
total = 0
while n <= 100:
    total += n
    n += 1

print()
print("总和为{}".format(total))
