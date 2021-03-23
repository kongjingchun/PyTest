# coding:utf-8
# @Create time: 2021/3/23 18:00
# @Author: KongJingchun
# @remark:

# 使用map函数，求元组 (2,4,6,8,10,12)中各个元素的5次方

# 任务
# 1、pow_five函数体内：计算元素的5次方
# 2、调用pow_five函数传入data，使用result接收


def pow_five(number_date):
    result = pow(number_date, 5)
    return result


if __name__ == '__main__':
    date = (2, 4, 6, 8, 10, 12)
    result = map(pow_five, date)
    print(list(result))

    # 简单方式
    result = map(lambda x: pow(x, 5), date)
    print(list(result))
