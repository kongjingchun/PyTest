# coding:utf-8
# @Create time: 2021/3/22 9:00 下午
# @Author: KongJingchun
# @remark:随机抽奖程序
import random
import time

gifts = ['ipad', 'iphone', 'mac', 'apple全家桶']


def choice_gift():
    gift = random.choice(gifts)
    print('恭喜你中了一个%s' % gift)


def choice_gift_new():
    number = random.randrange(0, 100, 1)
    print(number)
    if 0 <= number < 50:
        print('你中了一个ipad')
    elif 40 <= number < 70:
        print('你中了一个iphone')
    elif 70 <= number < 90:
        print('你中了一个mac')
    elif 90 <= number < 100:
        print('你中了apple全家桶')
    else:
        print('程序出错了，赶紧看看吧')


if __name__ == '__main__':
    for i in range(0, 10, 1):
        choice_gift_new()
        time.sleep(1)
