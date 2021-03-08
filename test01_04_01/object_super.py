# coding:utf-8
# @Create time: 2021/3/8 11:38 上午
# @Author: KongJingchun
# @remark:super练习

class Parent(object):
    def __init__(self):
        print('你好我是父亲')


class Child(Parent):
    def __init__(self):
        print('你好我是儿子')
        super().__init__()


if __name__ == '__main__':
    Child()
