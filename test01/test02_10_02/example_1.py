# coding:utf-8
# @Create time: 2021/5/25 12:26 上午
# @Author: KongJingchun
# @remark: 连接数据库

import mysql.connector

confiig = {
    "host": "49.233.5.13",
    "port": "3306",
    "user": "root",
    "password": "Jingchun0302!",
    "database": "demo",
    "auth_plugin": 'mysql_native_password'
}
con = mysql.connector.connect(**confiig)

cursor = con.cursor()
sql = "select empno, ename, sal, comm, deptno from t_emp;"
cursor.execute(sql)
cursor.fetchone()
for one in cursor:
    print(one[0], one[1], one[2], one[3], one[4])
con.close()
