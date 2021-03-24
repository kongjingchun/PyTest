# coding:utf-8
# @Create time: 2021/3/5 5:49 下午
# @Author: KongJingchun
# @remark: 类的多重继承

class Tool(object):
    def work(self):
        print('Tool在工作')

    def run(self):
        print('Tool在奔跑')


class Food(object):
    def work(self):
        print('Food在工作')

    def eat(self):
        print('Food在eat')


class Persoon(Tool, Food):
    pass


if __name__ == '__main__':
    p = Persoon()
    p.run()
    p.eat()
    p.work()
    print(Persoon.__mro__)
