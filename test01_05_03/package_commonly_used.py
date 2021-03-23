# coding:utf-8
# @Create time: 2021/3/22 8:16 下午
# @Author: KongJingchun
# @remark: 常用函数


# 输入信息到程序
# food = input('你想吃什么呢？')
# print(food)

# 判断对象中的所有属性是否都为True
if all([0 == 0, 1 == 1]):
    print('列表中结果都为True')

# 判断对象中是否有某个属性为True
if any([0 == 0, 0 == 1]):
    print('列表中有属性为True的 ')


class Test(object):
    a = 1
    b = 2


test = Test()
# hasattr获取对象属性是否存在
print(hasattr(test, 'a'))

# 给对象添加属性
setattr(test, 'name', '孔敬淳')
print(test.name)

# 获取对象的所有属性
print(vars(test))
