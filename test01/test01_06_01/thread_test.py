# coding:utf-8
# @Create time: 2021/3/24 7:29 下午
# @Author: KongJingchun
# @remark:多线程

import time
import random
import threading

lists = ['孔敬淳', '卢晓倩', '王野', '祁晓喆']
new_lists = []


def work():
    if len(lists) == 0:
        return
    data = random.choice(lists)
    new_data = '%s_new' % data
    lists.remove(data)
    new_lists.append(new_data)
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    t_list = []
    for i in range(len(lists)):
        # 创建线程
        t = threading.Thread(target=work)
        t_list.append(t)
        # 启动线程
        t.start()
    for t in t_list:
        # 阻塞线程
        t.join()
    print('old_list',lists)
    print('new_list',new_lists)
    print('总计耗时%s'% (time.time() -  start))