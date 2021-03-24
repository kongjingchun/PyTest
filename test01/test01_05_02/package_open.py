# coding:utf-8
# @Create time: 2021/3/18 5:23 下午
# @Author: KongJingchun
# @remark:文件和文件夹的读写
import os


def creat_package(path):
    if os.path.exists(path):
        raise Exception('%s已经存在了，不可创建' % path)
    os.mkdir(path)
    init_path = os.path.join(path, '__init__.py')
    f = Open(init_path)
    f.write('# codeing:utf-8')


class Open(object):
    def __init__(self, path, mode='w', is_return=True):
        self.path = path
        self.is_return = is_return
        self.mode = mode

    def write(self, message):
        f = open(self.path, 'w', encoding='utf-8')
        try:
            if self.is_return:
                message = '%s\n' % message
            f.write(message)
        except Exception as e:
            print(e)
        finally:
            f.close()

    def read(self, is_strip=True):
        _date = []
        with open(self.path, mode=self.mode, encoding='utf-8') as f:
            date = f.readlines()
        for i in date:
            if i != '':
                if is_strip:
                    _date.append(i.strip())
                else:
                    _date.append(i)
        return _date


if __name__ == '__main__':
    path = os.path.join(os.getcwd(), 'test')
    f = Open(path, mode='r')
    result = f.read(is_strip=True)
    print(result)
