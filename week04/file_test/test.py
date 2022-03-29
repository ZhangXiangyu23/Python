# coding:utf-8

"""
    join的使用
"""

import os

current_path = os.getcwd()
print(current_path)

# 测试使用join
path = os.path.join(current_path, "\lss.py")
print(path)