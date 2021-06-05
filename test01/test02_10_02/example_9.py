# coding:utf-8
# @Create time: 2021/5/25 12:26 上午
# @Author: KongJingchun
# @remark: 添加两个部门，使部门的deptno在原来最大值得基础上+10


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
    sql = "insert into t_dept (select max(deptno)+10,'A部门','北京' from t_dept union select max(deptno)+20,'B部门','北京' from t_dept);"
    cursor.execute(sql)
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
