# coding:utf-8
# @Create time: 2021/3/22 2:41 下午
# @Author: KongJingchun
# @remark:Base64加解密

import base64

replace_one = '%'
replace_two = '$'


def encode(date):
    if isinstance(date, str):
        date = date.encode('utf-8')
    elif isinstance(date, bytes):
        date = date
    else:
        raise TypeError('date需要时是bytes或str类型')
    _date = base64.encodebytes(date).decode('utf-8').replace('a', replace_one).replace('b', replace_two)
    return _date


def decode(date):
    _replace_one = replace_one.encode('utf-8')
    _replace_two = replace_two.encode('utf-8')

    if isinstance(date, bytes):
        _date = date.replace(_replace_one,b'a').replace(_replace_two,b'b')
        return base64.decodebytes(_date).decode('utf-8')
    else:
        raise TypeError('date需要是bytes类型')


if __name__ == '__main__':
    en_result = encode('孔敬淳')
    print(en_result)
    de_result = decode(en_result.encode('utf-8'))
    print(de_result)
