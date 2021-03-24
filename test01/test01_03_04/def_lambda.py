# coding:utf-8
# @Create time: 2021/2/25 11:02 上午
# @Author: KongJingchun
# @remark:匿名函数的定义

"""
定义一个没有返回值的匿名函数
"""
x = lambda: print('没有返回值的匿名函数被执行')
x()

"""
定义一个有返回值的匿名函数
"""
y = lambda x, y: x * y
print(y(2, 3))

"""
方法中调用匿名函数
"""
users = [
    {'name': 'xiaoqian'},
    {'name': 'wangye'},
    {'name': 'kongjingchun'}
]
users.sort(key=lambda x: x['name'])
print(users)
