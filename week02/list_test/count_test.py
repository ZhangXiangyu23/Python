# coding:utf-8

"""
    count函数：看看列表中有几个“参数”
"""

animals_list = ["dog", "cat", "dog", "tiger", "lion", "cat", "dog"]
print("The number of cat are %s" % animals_list.count("cat"))
print("The number of dog are {}".format(animals_list.count("dog")))
# num_tiger = animals_list.count("")
print(f'The number of tiger are{animals_list.count("tiger")}')

# 字典作为元素的列表
dict_list = [
    {"1": "python"},
    {"2": "math"},
    {"3": "c++"},
    {"1": "python"}
]

print(dict_list.count({"1": "python"}))

# count函数在元组中的使用
animals_tuple = ("elephant", "rabbit", "panda", "bird", "panda")
print(animals_tuple.count("panda"))
print(animals_tuple.count("bird"))
