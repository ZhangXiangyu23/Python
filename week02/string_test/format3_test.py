# coding:utf-8

"""
    使用三引号包裹字符串时，字符串中的格式能输出
    但是现实中不常使用这个
"""

info_01 = """
    123
    456
"""

print(info_01)

# \n的使用
info_02 = "I am\nzxy"
print(info_02)

# \t的使用 横向制表符
info_03 = "I am\tzxy"
print(info_03)

# \v  纵向制表符
info_04 = "I am \v zxy"
print(info_04)

# \a响铃声
info_05 = "\a"
print(info_05)

# \b 退格符，将光标前移，覆盖（删除前一个）  = 相当于删除符号
info_06 = "zxy\b"
print(info_06)

# \r 换行  （效果是:会将\r前面的字符串抹去，然后换行）
info_07 = "I am zxy\r123"
print(info_07)

# \f 翻页
print("999\f")

# 转义字符串中的引号
print("我是\"巨灵神\"")

print("I am \\  zxy")

# 在字符串前面加r,将字符串中的转义字符无效化
print(r"I am \\ lss\n")
