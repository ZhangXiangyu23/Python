# coding:utf-8

"""
    strip函数：如果没有参数的话，默认将字符串两侧的空格去掉
    如果有参数的话，是将字符串中的参数去掉
"""

info_01 = "     zhangxiangyu      "
print(info_01)
print(info_01.strip())

# 有参数的话
info_02 = "zxy"
print(info_02)
print(info_02.strip("z"))

"""
    lstrip函数，是将字符串左侧的子串去掉
"""

info_03 = "zxylss"
print(info_03)
print(info_03.lstrip("zx"))


"""
    rstrip函数，是将字符串右侧的子串去掉
"""
info_04 = "zxylssn"
print(info_04)
print(info_04.rstrip(info_04))
print("-----------------")