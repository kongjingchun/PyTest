# coding:utf-8
# @Create time: 2021/3/26 6:46 下午
# @Author: KongJingchun
# @remark: 正则表达式练习

import re


def check_url(url):
    result = re.findall('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+/', url)
    print(result)
    if len(result) != 0:
        return True
    else:
        return False


def get_url(url):
    result = re.findall('[a-zA-Z]{4,5}://(\w*\.*\w+\.\w+)/', url)
    if len(result) != 0:
        return result
    else:
        return ''


if __name__ == '__main__':
    url = 'https://www.imooc.com/'
    print(check_url(url))
    print(get_url(url))
