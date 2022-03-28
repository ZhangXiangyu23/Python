# coding:utf-8

"""
    时间戳，就是从1970年1月1日至今的时间间隔（单位为秒）
"""

# 导入time包
import time
import datetime


n = time.time()
print(n)
print(type(n))

# 将时间戳转化成一个时间对象
# 使用localtime函数将时间戳转化成一个时间对象
n_obj = time.localtime(n)
print(n_obj)
print(type(n_obj))

# 秒数转毫秒
t = time.time()
print(t * 1000)
print("-" * 100)
print(t)


"""
    sleep函数用来进行暂停
"""

# for i in range(10):
#     print(i)
#     time.sleep(1)

"""
    time对象类型转字符串
    字符串转time对象类型
"""

# 获取当前的时间戳
print("-" * 100)
zxy = time.time()
print(zxy)
# time对象转字符串
str_zxy = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(zxy))
print(str_zxy, type(str_zxy))

# 字符串转time对象
two_zxy = time.strptime(str_zxy, "%Y-%m-%d %H:%M:%S")
print("$" * 100)
print(two_zxy, type(two_zxy))

"""
    datetime类型转时间戳
    时间戳转成datetime类型
"""
# datetime类型转时间戳
g = datetime.datetime.now()
print(g, type(g))
g_1 = datetime.datetime.timestamp(g)
print(g_1, type(g_1))

# 时间戳转datetime类型
g_2 = datetime.datetime.fromtimestamp(g_1)
print(g_2, type(g_2))


