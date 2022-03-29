# coding:utf-8

"""
    通过一个类来实现自动创建一个python包
"""

import os


class AutoCreatP(object):
    def creat(self, path):
        if os.path.exists(path):
            raise Exception("该文件夹已经存在了，请勿重复创建")
        else:
            os.makedirs(path)
            f = open(path + "\__init__.py", "w")
            f.write("# coding:utf-8")
            f.close()




if __name__ == "__main__":
    # 实例化对象
    obj = AutoCreatP()
    # 获取当前路径
    current_path = os.getcwd()
    # 文件夹路径
    path = current_path + "\lss"
    obj.creat(path)



