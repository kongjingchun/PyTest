# coding:utf-8
# @Create time: 2021/3/1 4:10 下午
# @Author: KongJingchun
# @remark: 装饰器

class Test(object):
    def __init__(self, name):
        self._name = name

    def run(self):
        print('run')
        self.dump()

    @classmethod
    def dump(cls):
        print('dump')

    @staticmethod
    def sleep():
        print('sleep')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


a = Test('kjc')
a.run()
Test.sleep()
print(a.name)
a.name = 'kkk'
print(a.name)
