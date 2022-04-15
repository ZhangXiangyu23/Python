# coding:utf-8

import mysql.connector.pooling

"""
    executemany的使用
    相当于循环执行execute函数
"""
config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "zxy54321",
    "database": "vega"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    data = [["NBA"], ["教育"], ["感情"]]
    sql = "insert into t_type(type) values(%s)"
    cursor.executemany(sql, data)
    con.commit()
except Exception as e:
    if pool in dir():
        con.rollback()
    print(e)
