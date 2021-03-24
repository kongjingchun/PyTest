# coding:utf-8
# @Create time: 2021/3/23 12:46
# @Author: KongJingchun
# @remark:
from functools import reduce

frunts = ['apple', 'banana', 'orange']


def func(item):
    if 'e' in item:
        return True
    else:
        return False


# 返回符合条件的元素列表
result0 = filter(lambda x: 'e' in x, frunts)
print(list(result0))
result1 = filter(func, frunts)
print(list(result1))

# 根据条件判断列表中元素是否符合，返回正错列表
result2 = map(lambda x: 'e' in x, frunts)
print(list(result2))
result3 = map(func, frunts)
print(list(result3))
result = map(lambda x: pow(x, 5), (2, 3, 4, 5))
print(list(result))

# 批量转换列表中元素格式
list_1 = map(int, ['1', '2', '3', '4'])
print(list(list_1))
list_1 = map(int, [1, '2', 3, 4])
print(list(list_1))
list_1 = map(str, [1, '2', 3, 4])
print(list(list_1))
# 对列表中的数据进行累计操作
reduce_result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(reduce_result)
reduce_result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(reduce_result)
