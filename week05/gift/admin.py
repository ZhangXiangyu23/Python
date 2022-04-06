# coding:utf-8

import os
from base import Base
from common.error import NotUserError, UserActiveError, RoleError

class Admin(Base):
    # 多态：重写父类当中的__init__方法
    # 相当于声明了三个属性 username、user_json、gift_json
    # self.属性名相当于定义一个属性
    def __init__(self, username, user_json, gift_json):
        self.username = username
        # 使用super调用父类中的构造函数
        super().__init__(user_json, gift_json)
        self.get_user()


    def get_user(self):
        # 全部用户
        # 用户字典
        users = self._Base__read_users()
        # 当前用户名字是
        user = users.get(self.username)
        # 看看有没有这个用户
        if user == None:
            raise NotUserError("not user %s" % self.username)
        if user.get('role') != 'admin':
            raise RoleError('you are not admin')


        if user.get("active") == False:
            raise UserActiveError("%s 用户不可用" % self.username)
        # 设定类属性！！！
        self.user = user
        self.role = user.get('role')
        self.name = user.get('username')
        self.active = user.get('active')


    # 验证管理员身份
    def __check(self):
        self.get_user()
        if self.role != 'admin':
            raise Exception('permission')


    # 管理员添加人员
    def add_user(self, username, role):
        self.__check()
        # 类名+私有函数名
        self._Base__write_user(username=username, role=role)


    # 修改用户的活跃程度
    def update_user_active(self, username):
        self.__check()
        self._Base__change_active(username)


    # 更新用户的身份
    def update_user_role(self, username, role):
        self.__check()
        self._Base__change_role(username=username, role=role)

    # 添加礼物
    def add_gift(self, first_level, second_level, gift_name, gift_count):
        self.__check()
        self._Base__write_gifts(first_level=first_level, second_level=second_level,
                                gift_name=gift_name, gift_count=gift_count)


    # 管理员删除了礼物
    def delete_gift(self, first_level, second_level, gift_name):
        # 必须当前操作的用户是管理员才行啊
        self.__check()

        self._Base__delete_gift(first_level, second_level, gift_name)


    # 管理员更新礼物
    def gift_update(self, first_level, second_level, gift_name, gift_count):
        # 必须当前操作的用户是管理员才行啊
        self.__check()
        self._Base__gift_update(first_level=first_level, second_level=second_level,
                                gift_name=gift_name, gift_count=gift_count, is_admin=True)


if __name__ == "__main__":
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    admin = Admin(username="zxy", user_json=user_path, gift_json=gift_path)
    # admin.get_user()
    print("当前用户是", admin.name, admin.role)
    # admin.add_user('lxy', 'normal')
    # 改变用户活跃程度
    # admin.update_user_active('lxy')
    # admin.update_user_role(username='lss', role='admin')
    admin.gift_update(first_level='level1', second_level='level2', gift_name='iphone', gift_count=888)