# coding:utf-8

"""
    capitalize函数的用法:字符串变量.capitalize()
    将字符串中的首字母进行大写，剩下的其余字母无论是大写还是小写，全部变为小写!
    使用capitalize函数之后，产生的是新的字符串
"""

name = "zxy"
info_01 = "hello ZXY"
info_02 = "123zxY"
info_03 = "你好zxy"
info_04 = "Zxy yyds"

print(name.capitalize())  # Zxy
print(info_01.capitalize())  # Hello zxy
print(info_02.capitalize())  # 123zxy
print(info_03.capitalize())  # 你好zxy
print(info_04.capitalize())  # Zxy yyds


# 主函数
if __name__ == "__main__":
    """
        证明字符串是无法改变的，使用capitalize之后,产生的字符串地址和原字符串地址不一样
        是产生了一个新的字符串！
    """
    old_name = "lss"
    new_name = old_name.capitalize()
    print(id(old_name))
    print(id(new_name))