# coding:utf-8
# @Create time: 2021/5/25 12:26 上午
# @Author: KongJingchun
# @remark: 预防SQL注入

import mysql.connector

confiig = {
    "host": "49.233.5.13",
    "port": "3306",
    "user": "root",
    "password": "Jingchun0302!",
    "database": "vega",
    "auth_plugin": 'mysql_native_password'
}
con = mysql.connector.connect(**confiig)
cursor = con.cursor()
username = "1 or 1=1"
password = "1 or 1=1"
sql = "select * from t_user where username = %s and unhex(aes_decrypt(password,'HelloWorld'))  = %s;"
cursor.execute(sql,username,password)
print(cursor.fetchone())
con.close()
