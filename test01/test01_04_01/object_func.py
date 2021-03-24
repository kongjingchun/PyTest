# coding:utf-8
# @Create time: 2021/3/8 6:09 下午
# @Author: KongJingchun
# @remark: 类的高级函数 __str__ 和 __getattr__

class Test(object):
    def __str__(self):
        return '这个是方法的描述'

    def __getattr__(self, item):
        return '没有这个key:{}，并不存在！'.format(item)

    def __setattr__(self, key, value):
        print(key, value)

    def __call__(self, a):
        print(a)


t = Test()
print(t)
print(t.a)
t.name = 'kjc'
t('nihao')