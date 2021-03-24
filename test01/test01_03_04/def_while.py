# coding:utf-8
# @Create time: 2021/2/24 5:57 下午
# @Author: KongJingchun
# @remark:递归函数

count = 0
def test ():
    global count
    count +=1
    if count <5:
        print('还没到，目前执行到%s'%count)
        return test()
    else:
        print('已经执行到5了，退出了')

test()
