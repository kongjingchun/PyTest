# coding:utf-8
# @Create time: 2021/3/23 18:34
# @Author: KongJingchun
# @remark:
import random


class Game(object):
    min = None
    max = None
    correct_number = None

    def __init__(self, min, max):
        if not all([min.isdigit(), max.isdigit()]):
            exit('您输入的为非数字字符，请重新启动')
        self.min = int(min)
        self.max = int(max)
        if self.min == self.max:
            exit('您输入的区间数字相同!!!请重新启动程序')
        if self.min > self.max:
            exit('您输入的区间起始值大于区间终止值')

        self.correct_number = random.randint(self.min, self.max)
        print('所产生的随机数字区间为{}'.format([self.min, self.max]))

    def guess(self, number):
        if any([number > self.max, number < self.min]):
            print('对不起您输入的数字未在指定区间')
            return False
        if number == self.correct_number:
            return True
        if number > self.correct_number:
            print('您猜测的数字比结果大！')
            return False
        if number < self.correct_number:
            print('您猜测的数字比结果小！')
            return False


if __name__ == '__main__':
    print('*****************欢迎进入数字猜猜猜小游戏***********************')
    min = input('数字区间起始值')
    max = input('数字区间终止值')
    game = Game(min, max)
    guess_number = 0
    sucess = False
    while sucess == False:
        guess_number += 1
        u_number = input('请继续输入你猜测数字')
        if not u_number.isdigit():
            print('您猜测的为非数字字符，请重新输入')
        sucess = game.guess(int(u_number))
    print('恭喜你！只用了{}次就赢得了游戏'.format(guess_number))
