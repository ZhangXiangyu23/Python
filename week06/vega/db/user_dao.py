# coding:utf-8

from vega.db.mysql_db import pool

class UserDao:
    # 验证用户登录
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select count(*) from t_user where username=%s and" \
                  " AES_DECRYPT(UNHEX(password), 'lss')=%s"
            cursor.execute(sql, (username, password))
            count = cursor.fetchone()[0]
            # python中的三目运算
            return True if count == 1 else False
        except Exception as e:
            print(e)
        finally:
            if "con" is dir():
                con.close()

    # 查询用户角色
    def search_user_role(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "select r.role from t_user u join t_role r on u.role_id=r.id where u.username=%s"
            cursor.execute(sql, [username])
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if "con" is dir():
                con.close()
