# coding:utf-8
# @Create time: 2021/3/24 3:57 下午
# @Author: KongJingchun
# @remark: 进程池
import os
import multiprocessing
import time


def work(count,lock):
    lock.acquire()
    print(count, os.getpid())
    time.sleep(5)
    lock.release()
    return 'count is %s,pid is %s' % (count, os.getpid())


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)
    manager = multiprocessing.Manager()
    lock = manager.Lock()
    results = []
    for i in range(20):
        result = pool.apply_async(func=work, args=(i,lock))
        results.append(result)
    for res in results:
        print(res.get())
