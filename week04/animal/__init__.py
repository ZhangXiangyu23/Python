# coding:utf-8

"""
    可以导入包、可以导入模块、还可以导入函数
"""
# 我试试在__init__中导入函数
from .cat.action import run as cat_run
from .dog.action import run as dog_run

