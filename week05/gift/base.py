# coding:utf-8

from common.utils import check_file
import os
import json
import time
from common.error import UserExistsError, RoleError, LevelError, NegativeNumberError, NotExistError
from common.utils import timestamp_to_string
from common.consts import ROLES, FIRSTLEVELS, SECONDLEVELS

class Base(object):
    # 传入的参数应该是json文件的路径
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json= gift_json
        self.__check_user_json()
        self.__check_gift_json()
        self.__init_gifts()

    # 检查传入的文件是不是json文件
    def __check_user_json(self):
        check_file(self.user_json)

    # 方法名前面加__，表示私有方法
    def __check_gift_json(self):
        check_file(self.gift_json)


    def __read_users(self, time_to_str=False):
        with open(self.user_json, "r") as f:
            data = json.loads(f.read())
        if time_to_str == True:
            # username 是key, v是value
            for username, v in data.items():
                v['creat_time'] = timestamp_to_string(v['creat_time'])
                v['update_time'] = timestamp_to_string(v['update_time'])
                data[username] = v
        return data

    # **将传入的参数视为一个字典
    def write_user(self, **user):
        if 'username' not in user:
            raise TypeError("missing username")
        if 'role' not in user:
            raise TypeError("missing role")

        # 字典其他项
        user["active"] = True
        user["creat_time"] = time.time()
        user["update_time"] = time.time()
        user["gifts"] = []

        # 字典：其中关键字是username 然后对应值的数据类型也是字典
        # users = {
        #        "zxy":{},
        #        "lss":{}
        #
        # }

        users = self.__read_users()
        if user["username"] in users:
            raise UserExistsError('username %s had exists' % user['username'])

        users.update(
            {user["username"]: user}
        )

        # 将users字典转化成json格式
        self.__save(users, self.user_json)

    # 修改用户权限
    def __change_role(self, username, role):
        # 将整个数据都读出来
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        # 验证是否有这个角色
        if role not in ROLES:
            raise RoleError('not role %s' % role)
        user['role'] = role
        user['update_time'] = time.time()
        users[username] = user
        # 转成json格式
        self.__save(users, self.user_json)
        return True

    # 修改用户活跃程度
    def __change_active(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        # 修改key为username的字典（value）
        user['active'] = not user['active']
        # 修改时间
        user['update_time'] = time.time()

        # 修改大字典
        users[username] = user
        # 将大字典转成json格式
        self.__save(users, self.user_json)

    # 删除用户
    def delete_user(self, username):
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False

        delete_user = users.pop(username)
        self.__save(users, self.user_json)



    # 读取礼物
    def read_gifts(self):
        with open(self.gift_json, "r") as f:
            # 文件读出来，然后将json反序列化
            data = json.loads(f.read())
        return data


    # 初始化礼物
    def __init_gifts(self):
        data = {
            'level1':{
                'level1':{},
                'level2':{},
                'level3':{}
            },
            'level2': {
                'level1': {},
                'level2': {},
                'level3': {}
            },
            'level3': {
                'level1': {},
                'level2': {},
                'level3': {}
            },
            'level4': {
                'level1': {},
                'level2': {},
                'level3': {}
            }
        }

        gifts = self.read_gifts()
        if len(gifts) != 0:
            return

        # 将初始化数据序列化
        self.__save(data, self.gift_json)


    def write_gifts(self, first_level, second_level, gift_name, gift_count):
        if first_level not in FIRSTLEVELS:
            raise LevelError("firstlevel not exists")
        if second_level not in SECONDLEVELS:
            raise LevelError("secondlevel not exists")

        # 读出大字典
        gifts = self.read_gifts()
        # 第一层字典的value
        current_gift_pool = gifts[first_level]
        # 第二层字典的value
        current_second_gift_pool = current_gift_pool[second_level]
        # 其实第二层中的元素也是字典
        # 第二层中的元素
        # 'name1': {'name':xx, count:xx }, 'name2':{'name2':xx, count:xx}....

        if gift_count <= 0:
            gift_count = 1

        if gift_name in current_second_gift_pool:
            # 二级礼物池中具体的哪个礼物
            current_second_gift_pool[gift_name]['count'] = current_second_gift_pool[gift_name]['count'] + gift_count
        else:
            # 相当于新加
            current_second_gift_pool[gift_name] = {
                'name': gift_name,
                'count': gift_count
            }

        # 更新到大字典
        current_gift_pool[second_level] = current_second_gift_pool
        gifts[first_level] = current_gift_pool

        # 写回json文件库
        self.__save(gifts, self.gift_json)


    # 礼物更新
    def __gift_update(self, first_level, second_level, gift_name, gift_count=1):
        data = self.__check_and_getgift(first_level, second_level, gift_name)
        if data == False:
            return data

        gifts = data.get('gifts')
        current_second_gift_pool = data.get('level_two')
        current_gift_pool = data.get('level_one')

        # 最终的礼物字典
        current_gift = current_second_gift_pool[gift_name]

        # 如果传入的数量，本身数据库中就没有那么多，不能删除
        if current_gift['count'] - gift_count  < 0:
            raise NegativeNumberError("没有那么多的礼品")

        current_gift['count'] -= gift_count
        # 礼物字典回第二级
        current_second_gift_pool[gift_name] = current_gift
        # 第二级回第一级
        current_gift_pool[second_level] = current_second_gift_pool
        # 第一级回gifts
        gifts[first_level] = current_gift_pool
        self.__save(gifts, self.gift_json)


    # 删除具体的礼物
    def delete_gift(self, first_level, second_level, gift_name):
        data = self.__check_and_getgift(first_level, second_level, gift_name)
        if data == False:
            return data

        gifts = data.get('gifts')
        current_second_gift_pool = data.get('level_two')
        current_gift_pool = data.get('level_one')

        # 利用key将这个字典元素弹出
        # 礼物字典
        current_second_gift_pool.pop(gift_name)

        # 二级回一级
        current_gift_pool[second_level] = current_second_gift_pool
        gifts[first_level] = current_gift_pool
        # 保存
        self.__save(gifts, self.gift_json)

    # 将给定的数据进行序列化之后进行写入
    def __save(self, data, path):
        json_data = json.dumps(data)
        with open(path, "w") as f:
            f.write(json_data)


    def __check_and_getgift(self, first_level, second_level, gift_name):
        if first_level not in FIRSTLEVELS:
            raise LevelError("firstlevel not exists")
        if second_level not in SECONDLEVELS:
            raise LevelError("secondlevel not exists")

        # 读出大字典
        gifts = self.read_gifts()
        # 第一层字典的value
        level_one = gifts[first_level]
        # 第二层字典的value
        level_two = level_one[second_level]

        if gift_name not in level_two:
            return False

        return {
            'level_one': level_one,
            'level_two': level_two,
            'gifts': gifts
        }







if __name__ == "__main__":
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')

    print(gift_path)
    print(user_path)
    base = Base(user_json=user_path, gift_json=gift_path)
    # base.write_user(username="zxy", role="admin")
    # result = base.delete_user(username='zxy')
    # print(result)

    # result = base.read_gifts()
    # print(result)
    # base.init_gifts()
    # base.gift_update(first_level='level4', second_level='level2', gift_name="bag", gift_count=5)
    # base.delete_gift(first_level='level1', second_level='level2', gift_name="ipad")