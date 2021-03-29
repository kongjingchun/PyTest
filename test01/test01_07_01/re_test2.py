# coding:utf-8
# @Create time: 2021/3/26 6:46 下午
# @Author: KongJingchun
# @remark: 正则表达式练习

import re


def check_url(url):
    re_g = re.compile('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+/')
    result = re_g.findall(url)
    # print(result)
    if len(result) != 0:
        return True
    else:
        return False


def get_url(url):
    re_g = re.compile('[https://|http://](\w*\.*\w+\.\w+)/')
    result = re_g.findall(url)
    if len(result) != 0:
        return result
    else:
        return ''


def check_email(data):
    re_g = re.compile('.+@.+\.[a-zA-Z]+')
    result = re_g.findall(data)
    # result = re.findall('[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[a-zA-Z]+', data)
    if len(result) != 0:
        return True
    else:
        return False


def get_html_data(data):
    re_g = re.compile('style="(.*?)"')
    result = re_g.findall(data)
    return result


def get_all_htmi(data):
    re_g = re.compile('="(.+?)"')
    result = re_g.findall(data)
    return result


if __name__ == '__main__':
    url = 'http://www.imooc.com/'
    print(check_url(url))
    print(get_url(url))
    email = '411861376@qq.com'
    email = 'jing20130808@vip.qq.com'
    print(check_email(email))
    html = ('<div class="s-top-nav" style="display:none;">'
            '</div><div class="s-center-box"></div>')
    print(get_html_data(html))
    print(get_all_htmi(html))
    # 通过空格分割
    re_g = re.compile('\s')
    print(re_g.split(html))
    # 从开始匹配
    re_g = re.compile('<div class="(.+?)"')
    print('----------')
    print(re_g.match(html).group())
    # 获取匹配的位置
    print(re_g.match(html).span())
    print(html[:22])
