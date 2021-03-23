# coding:utf-8
# @Create time: 2021/3/22 4:53 下午
# @Author: KongJingchun
# @remark:定义log输出

import logging
import os


def init_log(path):
    if os.path.exists(path):
        mode = 'a'
    else:
        mode = 'w'
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
        filename='back.log',
        filemode=mode
    )
    return logging


if __name__ == '__main__':
    current_path = os.getcwd()
    path = os.path.join(current_path, 'back.log')
    log = init_log(path)
    log.error('error测试')
