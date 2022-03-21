# coding:utf-8

"""
    continue和break的使用
"""

info = [
    {"name": "zxy", "sex": "男"},
    {"name": "kaka", "sex": "男"},
    {"name": "lss", "sex": "女"}
]

man = []
for person in info:
    if person.get("sex") == "女":
        continue
    man.append(person)
    print("%s参加了活动" % person.get("name"))

print(man)

# 测试break
l = range(100)
for i in l:
    if i == 80:
        print("循环了80次了，停止循环")
    print(i)
else:
    print("循环正常退出了")  # 只要正常退出了，才执行

