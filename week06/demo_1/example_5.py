# coding:utf-8
import mysql.connector.pooling
"""
    删除的练习
"""

config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "zxy54321",
    "database": "hr8"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )



    con = pool.get_connection()
    sql = "truncate table position"
    cursor = con.cursor()
    cursor.execute(sql)
#     con.start_transaction()
#     cursor = con.cursor()
#     sql = "delete from position where level='部门员工'"
#     cursor.execute(sql)
#     con.commit()
except Exception as e:
#     if "con" in dir():
#         con.rollback()
    print(e)

