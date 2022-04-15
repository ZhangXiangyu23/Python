# coding:utf-8

import mysql.connector.pooling
"""
    数据库连接池
"""
# 写成字典格式或者说是json格式
config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "zxy54321",
    "database": "excellent"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sql = "update user set userPassword=%s where userName=%s"
    cursor.execute(sql, ("zhangxiangyu", "李姗珊"))
    con.commit()

except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
