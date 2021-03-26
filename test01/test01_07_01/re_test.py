# coding:utf-8
# @Create time: 2021/3/25 8:42 下午
# @Author: KongJingchun
# @remark: 正则表达式
import re


def had_number(data):
    # 匹配数字
    result = re.findall('\d', data)
    print(result)
    for i in result:
        return True
    return False


def remove_number(data):
    # 匹配非数字
    result = re.findall('\D', data)
    print(result)
    for i in result:
        return ''.join(result)
    return False


def startswith(sub, data):
    _sub = '\A%s' % sub
    result = re.findall(_sub, data)
    for i in result:
        return True
    return False


def endswith(sub, data):
    _sub = '%s\Z' % sub
    result = re.findall(_sub, data)
    if len(result) != 0:
        return True
    return False


def real_len(data):
    result = re.findall('\S', data)
    return len(result)


if __name__ == '__main__':
    data = 'Hello,my name is XiaoMu,i am 33'
    result = had_number(data)
    print(result)
    result = remove_number(data)
    print(result)
    result = startswith('Hello', data)
    print(result)
    result = endswith('33', data)
    print(result)
    print('_______________________')
    print(len(data))
    print(real_len(data))



    data1 = 'Hello,my name is 是 XiaoMu,i am 33'
    # 匹配数字
    print(re.findall('\d', data1))
    # 匹配英文
    print(re.findall('\D', data1))
    # 匹配空格及符号
    print(re.findall('\W', data1))
    # 从开始匹配字符串
    print(re.findall('\AHello', data1))
    # 从结尾匹配字符串
    print(re.findall('33\Z', data1))
    # 去除空格
    print(re.findall('\S', data1))
