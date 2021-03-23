# coding:utf-8
# @Create time: 2021/3/22 8:36 下午
# @Author: KongJingchun
# @remark:练习题
from functools import reduce


def my_func(x, y):
    return x + y


ages = [12, 13, 11, 19, 20]
res = reduce(my_func,ages)
print(res)
