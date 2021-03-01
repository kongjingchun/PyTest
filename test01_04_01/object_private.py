# coding:utf-8
# @Create time: 2021/3/1 3:25 下午
# @Author: KongJingchun
# @remark:私有变量和私有函数


class Cat(object):
    def __init__(self, name):
        self.name = name

    name = None

    def run(self):
        print(self.__run())

    def __run(self):
        return f'{self.name}在开心的跑着'


cat = Cat('小猫咪咪')
cat.run()
