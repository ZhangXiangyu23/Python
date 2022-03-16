# coding:utf-8

# 对字符串进行反转
info = "zxy"
# 类似于列表的反序
print(info[::-1])

"""
    find函数和index函数都是返回参数值在原字符串中的索引位置
    区别是：find如果找不到的话，就会返回-1
          index如果找不到的话，就会报错的
"""

result = info.find("lss")
print(result)
# print(info.index("lss"))

