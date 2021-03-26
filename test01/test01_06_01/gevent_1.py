# coding:utf-8
# @Create time: 2021/3/25 5:44 下午
# @Author: KongJingchun
# @remark: geven异步的使用

import gevent
import time
import random


def gevent_a():
    for i in range(5):
        print(i, 'a')
        gevent.sleep(random.random() * 2)
    return 'gevent a'


def gevent_b():
    for i in range(5):
        print(i, 'b')
        gevent.sleep(random.random() * 2)
    return 'gevent b'


if __name__ == '__main__':
    start = time.time()
    # 创建gevent异步
    g_a = gevent.spawn(gevent_a)
    g_b = gevent.spawn(gevent_b)
    gevent_list = [g_a, g_b]
    # 执行gevent异步
    result = gevent.joinall(gevent_list)
    print(result[0].value)
    print(result[1].value)
    print(time.time() - start)
