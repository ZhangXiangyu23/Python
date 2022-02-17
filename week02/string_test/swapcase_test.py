# coding:utf-8
"""
swapcase函数是将字符串中的大写字母转化成小写字母
将小写字母转化成大写字母
"""


info_one = 'ZhangXiangYu'
# 在这里等价于lower函数
info_two = 'ZHANGXIANGYU'
# 这里等价于upper函数
info_three = 'zhangxiangyu'

info_one_new = info_one.swapcase()
info_two_new = info_two.swapcase()
info_three_new = info_three.swapcase()

print(info_one_new)
print(info_two_new)
print(info_three_new)