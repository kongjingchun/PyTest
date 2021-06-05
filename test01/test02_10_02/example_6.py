# coding:utf-8
# @Create time: 2021/5/25 12:26 上午
# @Author: KongJingchun
# @remark: 删除语句

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
    sql = "delete e,d from t_emp as e join t_dept as d on e.deptno = d.deptno where d.deptno = 20;"
    cursor.execute(sql)
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
