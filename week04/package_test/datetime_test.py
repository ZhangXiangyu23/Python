# coding:utf-8

from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now)
print(type(now))
# 时间间隔
three_day = timedelta(days=3)
# 三天之后
print(now + three_day)
# 三天之前
print(now - three_day)

# 测试小时
one_hour = timedelta(hours=1)
# 一个小时之后
print(now + one_hour)

# 将datetime格式转化成字符串格式
n = datetime.now()
print(n, type(n))
new_n = n.strftime("%Y/%m/%d %H:%M:%S")
print(new_n, type(new_n))

# 将字符串转化成datetime类型
n_obj = datetime.strptime(new_n, "%Y/%m/%d %H:%M:%S")
print(n_obj)
print(type(n_obj))

print("-" * 100)
zxy = datetime.now()
print(zxy, type(zxy))
zxy_new = zxy.strftime("%Y/%m/%d")
print(zxy_new, type(zxy_new))
# 字符串转datetime类型
str_zxy = datetime.strptime(zxy_new, "%Y/%m/%d")
# datetime类型格式是2022-03-28 00:00:00这种类型
# 但是字符串只有年月日，所以按datetime类型输出的话，就是自动填充时分秒为00:00:00
print(str_zxy, type(str_zxy))
