# coding:utf-8
# @Create time: 2021/3/23 17:39
# @Author: KongJingchun
# @remark:

# 使用filter函数，求0-50以内（包括50）的偶数
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

# 任务
# 1、定义use_filter函数
# 2、函数体内：实现过滤偶数值的功能
def use_filter(date):
    return filter(lambda x: x % 2 == 0, date)


if __name__ == '__main__':
    date = list(range(51))
    result = use_filter(date)
    print(list(result))
