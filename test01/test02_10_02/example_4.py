# coding:utf-8
# @Create time: 2021/5/25 12:26 上午
# @Author: KongJingchun
# @remark: 异常处理、开启事务

import mysql.connector

confiig = {
    "host": "49.233.5.13",
    "port": "3306",
    "user": "root",
    "password": "Jingchun0302!",
    "database": "demo",
    "auth_plugin": 'mysql_native_password'
}
try:
    con = mysql.connector.connect(**confiig)
    con.start_transaction()
    cursor = con.cursor()
    sql = "insert into t_emp(empno,ename, job, mgr, hiredate, sal, comm, deptno) values (%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(sql, (666, "kjc", "admin", 7839, "2020-02-20", 666, 666, 10))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
finally:
    if "con" in dir():
        con.close()
