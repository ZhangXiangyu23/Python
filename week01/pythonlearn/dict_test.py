# coding:utf-8

# 练习使用字典
user_info = {'name': 'zxy', 'age': 18, 'height': 180}

result = 'name' in user_info
print(result)

# 识别的是字典中的key
result = 'zxy' in user_info
print(result)

length = len(user_info)
print(length)

dict_test = {}
print(bool(dict_test))
dict_test = {'name': 'zxy', 'name1': 'lss'}
print(bool(dict_test))
print(type(dict_test))
# 判断依据是key,返回的也是key
print(max(user_info))
print(min(user_info))