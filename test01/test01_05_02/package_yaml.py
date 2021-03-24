# coding:utf-8
# @Create time: 2021/3/19 5:30 下午
# @Author: KongJingchun
# @remark:

import yaml


def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        _result = f.read()
    return yaml.load(result, Loader=yaml.FullLoader)


if __name__ == '__main__':
    result = read('muke.yaml')
    print(result)
