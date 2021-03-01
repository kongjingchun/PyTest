# coding:utf-8
# @Create time: 2021/3/1 4:10 下午
# @Author: KongJingchun
# @remark: 装饰器

def check_str(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 'ok':
            return 'result is %s' % result
        else:
            return 'result is failed:%s' % result
    return inner


@check_str
def test(st):
    return st


result = test('ok')
print(result)
