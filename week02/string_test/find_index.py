# coding:utf-8

info = 'zhangxiangyu'
# find的使用
# 在字符串中能找到子串，返回子串所在原串中的首字母索引（从0开始）
# 没有找到，返回-1
print(info.find('an'))
print(info.find('ok'))


# index的使用
# 在原字符串中寻找子串所在的索引位置，找到之后返回
# 如果在原字符串中找不到，就会报错
print(info.index('an'))
print(info.index('ok'))
