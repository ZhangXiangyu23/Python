# coding:utf-8

"""
    elif的使用
"""

num = -8

if num > 10:
    print("这个数大于10")
elif 5 <= num <= 10:
    print("这个数在5~10之间")
elif 0 <= num < 5:
    print("这个数在0~4之间")
else:
    print("这个数为负数")

# 用列表和字典进行解决
# 使用列表
info = [
    ("zxy", 99),
    ("lss", 99),
    ("kaka", 83)
]

# 新同学
# 联系elif
stu = ["lss", 98]
if info[0] == stu[0]:
    stu[0] = "%s_new" % stu[0]
    info.append(stu)
elif info[1] == stu[0]:
    stu[0] = "%s_new" % stu[0]
    info.append(stu)
else:
    stu[0] = "%s_new" % stu[0]
    info.append(stu)

print(info)


# 使用字典来解决
dict = {
    "zxy": {"score": 100},
    "lss": {"score": 99},
    "lxy": {"score": 88}
}

print(dict)
if stu[0] in dict:
    stu[0] = "%s_new" % stu[0]
else:
    dict[stu[0]] = {"score": stu[1]}

print(dict)

