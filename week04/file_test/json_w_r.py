# coding:utf-8

"""
    将字典类型转成json格式，然后写入文件中
"""

import json

# 将字典序列化并写入
def write(path, data):
    with open(path, "w") as f:
        if isinstance(data, dict):
            f.write(json.dumps(data))
        else:
            raise Exception("该数据的类型不是字典类型")

# 将json格式的内容读出
def read():
    with open("test.txt", "r") as f:
        # 反序列化
        return json.loads(f.read())


# 字典
info = {
    'name': 'zxy',
    'age': 18,
    'book': 'python',
    'height': 180
}


if __name__ == "__main__":
    # write("test.txt", info)
    result = read()
    print(result, type(result))
    # 在字典中添加key-value
    result["sex"] = "boy"
    # 重新写入
    write("test.txt", result)
