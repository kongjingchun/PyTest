# coding:utf-8
# @Create time: 2021/3/23 18:26
# @Author: KongJingchun
# @remark:

# 请运用reduce函数，计算20的阶乘，并于终端打印计
# 算结果（如下）
from functools import reduce


def use_reduce(x, y):
    result = x * y
    return result


if __name__ == '__main__':
    date = list(range(1, 21, 1))
    result = reduce(use_reduce, date)
    print(result)
