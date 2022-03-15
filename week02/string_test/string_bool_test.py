# coding:utf-8

"""
    isspace函数：判断字符串是否为空格
    istitle函数:判断字符串是否为标题（只针对英文，必须是每个单词首字母大写，其他不大写）
    isupper函数：判断字符串中字符是否全是大写（不管那些非字母）
    islower函数:判断字符串中字符是否全是小写（不管那些非字母）
"""

info_01 = "  "
info_02 = "I Am Zxy"
info_03 = "ZXYLSS哈哈哈哈!"
info_04 = "zxy@@"


if __name__ == "__main__":
    print(info_01.isspace())
    print(info_02.istitle())
    print(info_03.isupper())
    print(info_04.islower())