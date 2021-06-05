# coding:utf-8
# @Create time: 2021/5/25 12:26 上午
# @Author: KongJingchun
# @remark:  使用INSERT语句，把部门平均底薪超过公司平均底薪的这样的部门里的员工信息倒入到t_emp_new表里面，并且让这些员工隶属于sales部门

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
    sql = "drop table t_emp_new;"
    cursor.execute(sql)
    sql = "create table t_emp_new like t_emp;"
    cursor.execute(sql)
    sql = "select avg(sal) from t_emp;"
    cursor.execute(sql)
    temp = cursor.fetchone()
    avg = temp[0]  # 公司平均底薪
    sql = "select deptno from t_emp group by deptno having avg(sal)>=%s;"
    cursor.execute(sql, [avg])
    temp = cursor.fetchall()
    sql = "insert into t_emp_new select * from t_emp where deptno in ("
    for index in range(len(temp)):
        one = temp[index][0]
        if index < len(temp) - 1:
            sql += str(one) + ","
        else:
            sql += str(one)
    sql += ")"
    print(sql)
    cursor.execute(sql)
    # for one in cursor:
    #     print(one[0])
    sql = "select deptno from t_dept where dname = %s"
    cursor.execute(sql, ["sales"])
    deptno = cursor.fetchone()
    print(deptno)
    sql = "update t_emp_new set deptno = %s;"
    cursor.execute(sql, deptno)

    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
