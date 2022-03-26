# coding

"""
    递归函数（自己调用自己）
    1.递归入口
    2.递归
    3.递归出口
"""


count = 0
def Test():
    global count
    count += 1
    if count < 5:
        print(f"{count},不满足条件")
        return Test()
    else:
        print("OK,结束！")


if __name__ == "__main__":
    Test()
