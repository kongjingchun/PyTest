# coding:utf-8
# @Create time: 2021/3/5 5:49 下午
# @Author: KongJingchun
# @remark: 类的继承

class Parent(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def takl(self):
        return f'{self.name}在说话'


class Child(Parent):
    def run(self):
        return f"{self.name}在奔跑"


child = Child('kjc', 'boy')
print(child.run())
print(child.takl())
