# coding:utf-8

import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1", port="3306",
    user="root", password="zxy54321",
    database="excellent"
)

cursor = con.cursor()
select_sql = "select * from user"
cursor.execute(select_sql)

# 输出
for item in cursor:
    print(item[0], item[1])
con.close()