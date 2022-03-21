# coding:utf-8

"""
    if语句的使用
"""

info = "My name is zxy"
# 不传参数的话，默认按照空格进行分割
info_list = info.split()
print(info_list)

# 模拟字符串替换的过程
n = 0
while n < len(info_list):
    if info_list[n] == "zxy":
        info_list[n] = "lss"
    n += 1


print("替换之后的结果是", info_list)
print(info)

# 将列表中的值，重新拼接成字符串
print("重新拼接之后")
print(" ".join(info_list))

# replace函数的测试
result = "zxy and lss"
print(len(result))

if len(result) > 10 and len(result) != 11:
    print(result.replace("and", "love"))