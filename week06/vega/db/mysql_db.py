# coding:utf-8

import mysql.connector.pooling
"""
    数据库连接池
"""

__config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "zxy54321",
    "database": "vega"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=30
    )

except Exception as e:
    print(e)

