# coding:utf-8
# @Create time: 2021/5/25 12:26 上午
# @Author: KongJingchun
# @remark: 循环执行SQL语句

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
    sql = "insert into t_dept (deptno, dname, loc)values (%s,%s,%s);"
    data = [[100, "会计部", "北京"], [200, "技术部", "北京"]]
    cursor.executemany(sql, data)
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
