# coding:utf-8
# @Create time: 2021/3/18 11:01 上午
# @Author: KongJingchun
# @remark: time包的使用

import time

now = time.time()
print(now)

time_date = time.localtime()
print(time_date)

for i in range(3):
    time.sleep(1)
    print(i)
