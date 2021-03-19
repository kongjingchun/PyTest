# coding:utf-8
# @Create time: 2021/3/19 4:35 下午
# @Author: KongJingchun
# @remark: json练习

import json


def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


def write(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        if isinstance(data, dict):
            f.write(json.dumps(data))
        else:
            raise TypeError('data应该为dick类型')
        return True


if __name__ == '__main__':
    data = {'name': '孔敬淳', 'age': 18, 'top': 183}
    write('test.json', data)
    read_data = read('test.json')
    print(read_data)
    read_data['sex'] = 'boy'
    write('test.json', read_data)
    read_data = read('test.json')
    print(read_data)
