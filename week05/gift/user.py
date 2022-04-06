# coding:utf-8

from base import Base
from common.error import NotUserError, RoleError, UserActiveError, CountError
from common.utils import timestamp_to_string
import os
import random

class User(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username
        self.gift_random = list(range(1, 101))
        super().__init__(user_json=user_json, gift_json=gift_json)
        self.get_user()


    def get_user(self):
        users = self._Base__read_users()
        # 这个key不在users字典中的话
        if self.username not in users:
            raise NotUserError("not user %s" % self.username)


        # 看看它的身份
        current_user = users.get(self.username)
        # 身份是否冻结
        if current_user.get("active") == False:
            raise UserActiveError("%s 用户不可用" % self.username)
        if current_user.get('role') != 'normal':
            raise RoleError('you are not normal')

        self.user = current_user
        self.name = current_user.get('username')
        self.role = current_user.get('role')
        self.gifts = current_user.get('gifts')
        self.creat_time = timestamp_to_string(current_user.get('creat_time'))


    # 给用户显示有哪些礼物
    def get_gifts(self):
        gifts = self._Base__read_gifts()
        gifts_lists = []
        for level_one, level_one_pool in gifts.items():
            for level_two, level_two_pool in level_one_pool.items():
                for gift_name, gift_info in level_two_pool.items():

                    gifts_lists.append(gift_name)
        return gifts_lists


    def chioce_gift(self):
        # 动态验证身份
        self.get_user()
        first_level, second_level =None, None
        level_one_count = random.choice(self.gift_random)
        print("-" * 100)
        print(level_one_count)
        if 1 <= level_one_count <= 50:
            first_level = 'level1'
        elif 51 <= level_one_count <= 80:
            first_level = 'level2'
        elif 81 <= level_one_count <= 95:
            first_level = 'level3'
        elif level_one_count > 95:
            first_level = 'level4'
        else:
            raise CountError("level_one_count need 1~100")

        gifts = self._Base__read_gifts()
        # 第一层礼物池中寻找
        level_one = gifts.get(first_level)
        print(level_one)

        # 第二层
        level_two_count = random.choice(self.gift_random)
        print(level_two_count)
        if 1 <= level_two_count <= 80:
            second_level = 'level1'
        elif 81 <= level_two_count < 95:
            second_level = 'level2'
        elif 95 <= level_two_count <= 100:
            second_level = 'level3'
        else:
            raise CountError("level_two_count need 1~100")
        level_two = level_one.get(second_level)
        print(level_two)
        if len(level_two) == 0:
            print("哦可惜，您没有中奖啊")
            return
        gift_names = []
        # 遍历第二层礼物池子，将第二层的礼物全部放到礼物列表中
        for k, _ in level_two.items():
            gift_names.append(k)

        # 第二层礼物池子中随机选一个
        gift_name = random.choice(gift_names)
        # print("*" * 100)
        # print(gift_name)
        # 找到第二层礼物池子中对应的礼物
        gift_info = level_two.get(gift_name)
        if gift_info.get('count') <= 0:
            print("好兄弟，中奖了，但是前面的礼物被抽完了")

        # 礼物池子中对应礼物数量--
        gift_info['count'] -= 1
        # 回填
        level_two[gift_name] = gift_info
        level_one[second_level] = level_two
        gifts[first_level] = level_one
        self._Base__save(gifts, self.gift_json)
        self.user['gifts'].append(gift_name)
        self.update()
        print("恭喜您获得 %s 奖品" % gift_name)


    def update(self):
        users = self._Base__read_users()
        users[self.username] = self.user

        self._Base__save(users, self.user_json)




if __name__ == "__main__":
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    # 实例化user类
    user = User("lxy", user_path, gift_path)
    # 输出属性
    print(user.name, user.creat_time, user.gifts, user.role)

    # 有哪些礼物
    result = user.get_gifts()
    print(result)
    user.chioce_gift()
