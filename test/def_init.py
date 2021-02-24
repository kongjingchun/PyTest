# coding:utf-8
# @Create time: 2021/2/24 3:05 下午
# @Author: KongJingchun
# @remark: 定义一个首字母大写的方法

def oneup(data):
    index = 0
    temp = ''
    for item in data:
        if index == 0:
            temp = item.upper()
        else:
            temp += item
        index += 1
    return temp


c = oneup('hello,孔敬淳')
print(c)
