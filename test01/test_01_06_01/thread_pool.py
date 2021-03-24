# coding:utf-8
# @Create time: 2021/3/24 23:20
# @Author: KongJingchun
# @remark:线程池

from concurrent.futures import ThreadPoolExecutor
import time
import threading

t_lock = threading.Lock()


def work(i):
    t_lock.acquire()
    print(i)
    time.sleep(1)
    t_lock.release()


if __name__ == '__main__':
    t_loop = ThreadPoolExecutor(2)
    for i in range(20):
        t_loop.submit(work, (i,))
