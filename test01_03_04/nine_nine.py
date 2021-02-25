# coding:utf-8
# @Create time: 2021/2/23 6:42 下午
# @Author: KongJingchun
# @remark: 九九乘法表

for i in range(1, 10):
    j = 1
    while j < i + 1:
        print('{} * {} = {}'.format(j, i, i * j), end=' ')
        j += 1
    print()
print('配置测试提交')