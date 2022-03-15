# coding:utf-8

"""
    各种格式化字符
"""

print("%c" % "c")
print("%u" % -8)
print("%d" % 123)
print("%f" % 3.14)
print("%f" % 10)


"""
    格式化中的进制
"""

# 以10进制输出
print("%d" % 12)
# 以8进制输出
print("%o" % 8)
# 以16进制输出
print("%x" % 48)


# 小技巧之：16进制和10进制的相互转化
num = int("123abc", 16)
print(num)
print("%x" % num)

# 科学计数法
print("%e" % 120000)