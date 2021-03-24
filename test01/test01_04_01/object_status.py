# coding:utf-8
# @Create time: 2021/3/8 5:35 下午
# @Author: KongJingchun
# @remark:类的多态

class XiaomuFather(object):
    def talk(self):
        print('小慕的父亲在说话')


class XiaoMu(XiaomuFather):
    def talk(self):
        print('小慕在说话')


if __name__ == '__main__':
    xiaomu = XiaoMu()
    xiaomu.talk()
