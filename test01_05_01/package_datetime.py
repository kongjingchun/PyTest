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
