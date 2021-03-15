# coding:utf-8
# @Create time: 2021/3/15 6:22 下午
# @Author: KongJingchun
# @remark:异常捕获

def upper(str_date):
    new_str = ''
    try:
        new_str = str_date.upper()
    except Exception as e:
        print('程序报错了')
        print(e)
    return new_str


new_str = upper(123)
print(new_str)
