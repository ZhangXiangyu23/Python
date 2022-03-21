# coding:utf-8

"""
    bytes类型和字符串类型的转化
    bytes类型就是在字符串类型前面加个b
"""

info = "I am zxy"
print(info)
print(type(info))

info_01 = b"i am zxy"
print(info_01)
print(type(info_01))

# 对bytes类型使用一些字符串的内置函数
# capitalize内置函数可以用，功能是将字符串中的首字母进行大写
print(info_01.capitalize())
# 使用replace函数
print(info_01.replace(b"zxy", b"lss"))

# 对bytes使用索引,会返回一个数字
print(info_01[0])
# 对bytes类型进行切片,可以进行切片，切片之后返回的也是一个bytes类型
print(info_01[:3])
# bytes类型使用find函数
print(info_01.find(b"i"))

# 使用内置函数dir来打印bytes类型的属性和方法
print(dir(info_01))

"""
    encode:编码（字符串类型转bytes类型）
    decode:解码（bytes类型转成字符串类型）
    使用这两个函数来进行编解码
"""

info_02 = "I am 李姗珊"
new_info_02 = info_02.encode("utf-8")
print(new_info_02)
print(type(new_info_02))
# 解码
print(new_info_02.decode("utf-8"))

print(dir(info_02))
print("---------------------")
print(dir(new_info_02))