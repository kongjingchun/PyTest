# coding:utf-8
# @Create time: 2021/5/25 12:26 上午
# @Author: KongJingchun
# @remark: 连接池

import mysql.connector.pooling

config = {
    "host": "49.233.5.13",
    "port": "3306",
    "user": "root",
    "password": "Jingchun0302!",
    "database": "demo",
    "auth_plugin": 'mysql_native_password'
}
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(**config, pool_size=10)
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sql = "update t_emp set sal = sal+%s where deptno = %s;"
    cursor.execute(sql, (200, 20))
    con.commit()
    print(111111)
except Exception as e:
    print('1111111')
    if "con" in dir():
        con.rollback()
    print(e)
