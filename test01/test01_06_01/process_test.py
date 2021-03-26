# coding:utf-8
# @Create time: 2021/3/24 11:45 上午
# @Author: KongJingchun
# @remark:进程的操作
import time
import os
import multiprocessing


def work_a():
    for i in range(3):
        print(i, 'a', os.getpid())
        time.sleep(1)


def work_b():
    for i in range(5):
        print(i, 'b', os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    # 创建进程
    a_p = multiprocessing.Process(target=work_a)
    # 启动进程
    # a_p.start()
    b_p = multiprocessing.Process(target=work_b)
    # b_p.start()
    for p in (a_p, b_p):
        p.start()

    for p in (a_p, b_p):
        p.join()

    for p in (a_p, b_p):
        # 判断进程是否还存在
        print(p.is_alive())

    print('时间消耗：', time.time() - start)
    print('parent pid is %s' % os.getpid())
