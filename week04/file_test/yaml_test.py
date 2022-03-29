# coding:utf-8

"""
    读取yaml文件
"""

import yaml

def read(path):
    with open(path, "r") as f:
        data = f.read()
        # 使用yaml的load函数进行解析
        result = yaml.load(data, Loader=yaml.FullLoader)
        return result
        # return data


if __name__ == "__main__":
    result = read("about.yaml")
    print(result)