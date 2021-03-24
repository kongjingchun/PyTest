# coding:utf-8
# @Create time: 2021/3/22 9:37 下午
# @Author: KongJingchun
# @remark:迭代器


# 迭代器会报错
# iter_obj = iter([1, 2, 3])
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

def test():
    for i in range(10):
        yield i


# 迭代器不会报错
# res = test()
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

# 对迭代器进行循环，循环结束后退出，不会报错
# res = test()
res = (i for i in range(5))
for item in res:
    print(item)



