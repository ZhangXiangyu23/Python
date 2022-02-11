# coding=utf-8

name = "张翔宇"
age = 18
weight = 75.5

"""
if __name__ == "__main__":
这句代码有什么用呢？
这句代码相当于C或者java中的主函数（整个文件的入口程序）
只能在当前文件执行代码块中的内容
将本文件导入其他文件中的时候，if __name__ == "__main__":
后面的代码不会执行！
"""

if __name__ == "__main__":
    print(name)
    print(age)
    print(weight)


