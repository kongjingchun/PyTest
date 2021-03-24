# coding:utf-8
# @Create time: 2021/3/22 8:40 下午
# @Author: KongJingchun
# @remark: 随机函数

import random

# 返回0～1之间的随机浮点数
print(random.random())
# 返回a～b区间的随机浮点数
print(random.uniform(1, 10))
# 返回a～b区间的一个随机整数,不包含10
print(random.randint(1, 10))
# 返回一个对象中的随机元素
print(random.choice('abc'))
print(random.choice([1, 2, 3]))
print(random.choice((1, 2, 3)))
# 返回对象中指定个数的元素
print(random.sample([1, 2, 3, 4, 5, 6], 2))
print(random.sample('abcdef', 2))
# 获取区间内的一个随机数(下个方法为解释)
print(random.randrange(0, 10, 2))
# 上面方法类似
print(random.choice(range(0, 10, 2)))

print('________________________')
print(random.randint(1, 2))