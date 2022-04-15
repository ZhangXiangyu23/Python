# coding:utf-8

import mysql.connector
config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "zxy54321",
    "database": "vega"
}

con = mysql.connector.connect(**config)
username = "1 OR 1=1"
password = "1 OR 1=1"
# 如果不加空格的话,字符串拼接之后，1就会和AND连在一起，sql语句出错
sql = "select count(*) from t_user where username="+username+" AND AES_DECRYPT(UNHEX(password),'lss')="+password
# sql = "select * from t_user"
cursor = con.cursor()
cursor.execute(sql)
print(cursor.fetchone()[0]) # 会输出2,因为t_user表中有两条数据
con.close()
