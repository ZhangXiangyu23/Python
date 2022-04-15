# coding:utf-8

import mysql.connector

try:
    con = mysql.connector.connect(
        host= "localhost",
        port= 3307,
        user= "root",
        password= "zxy54321",
        database= "excellent"
    )
    con.start_transaction()
    cursor = con.cursor()
    sql = "insert into user(userName, useraccount, userPassword, types, graID)" \
          "values(%s, %s, %s, %s, %s)"
    cursor.execute(sql, ("李姗珊", "181300", "zxylss", 2, 50))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
finally:
    if "con" in dir():
        con.close()