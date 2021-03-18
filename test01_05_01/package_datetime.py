# coding:utf-8
# @Create time: 2021/3/17 9:09 下午
# @Author: KongJingchun
# @remark: datetime包的使用

from datetime import datetime
from datetime import timedelta

now = datetime.now()
one_day = timedelta(days=1)
print(now)
print(one_day)
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_str, type(now_str))
now_date = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S')
print(now_date, type(now_date))
date_str = '2018 03 15'
date = datetime.strptime(date_str, '%Y %m %d')
print(date)

# 课后习题
# 定义now_变量接收当前日期时间
now = datetime.now()
# 计算当前日期时间3天6小时12分钟之前的日期时间
now_before = now - timedelta(days=3, hours=6, minutes=12)
# 计算当前日期时间10天之后的日期时间
now_after = now + timedelta(days=10)
print('--------------------------------')
print(now_before)
print(now_after)

# 获取时间戳
a = datetime.timestamp(datetime.now())
print(a)
# 时间戳转换为时间格式
b = datetime.fromtimestamp(a)
print(b)
