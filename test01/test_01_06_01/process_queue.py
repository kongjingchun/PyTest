# coding:utf-8
# @Create time: 2021/3/24 6:04 下午
# @Author: KongJingchun
# @remark:
import time
import json
import multiprocessing


class Work(object):
    def __init__(self, q):
        self.q = q

    def send(self, message):
        if not isinstance(message, str):
            message = json.dumps(message)
        self.q.put(message)

    def receive(self):
        # i = 0
        while 1:
            # i += 1
            result = self.q.get()
            try:
                res = json.loads(result)
            except:
                res = result
            print('reve is %s' % res)
            # print(i)

    def send_all(self):
        for i in range(10):
            self.q.put(i)
            time.sleep(1)


if __name__ == '__main__':
    # 创建队列
    q = multiprocessing.Queue()
    work = Work(q)
    # 创建进程，并传入队列
    send = multiprocessing.Process(target=work.send, args=({'name': '孔敬淳'},))
    send_all = multiprocessing.Process(target=work.send_all)
    rece = multiprocessing.Process(target=work.receive)
    # 启动进程
    send_all.start()
    send.start()
    rece.start()
    # 阻塞进程
    send_all.join()
    # 结束进程
    rece.terminate()  # 并不会立即关闭进程，有个等着操作系统去关闭这个进程的时间
    time.sleep(3)
    print(rece.is_alive())

