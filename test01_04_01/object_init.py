# @Create time: 2021/3/1 2:37 下午
# @Author: KongJingchun
# @remark:类的实例化

# coding:utf-8
class Person(object):
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    name = None
    age = None

    def run(self):
        print(f'{self.name}在奔跑')


kjc = Person('kjc', 30)
kjc.run()
