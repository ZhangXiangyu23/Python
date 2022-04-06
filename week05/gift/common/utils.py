# coding:utf-8

import os
from .error import NotPathError, NotFilePath, FormatError
import time


def timestamp_to_string(timestamp):
    # localtime函数是将时间戳类型转化成struct_time对象
    time_obj = time.localtime(timestamp)
    # 将struct_time对象进行格式化，然后返回一个字符串
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
    return time_str



def check_file(path):
    if not os.path.exists(path):
        raise NotPathError("not found %s" % path)

    if not path.endswith('.json'):
        raise FormatError("need json format")

    if not os.path.isfile(path):
        raise NotFilePath("this is a not file")
