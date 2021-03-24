# coding:utf-8
# @Create time: 2021/3/22 10:50 上午
# @Author: KongJingchun
# @remark:Hash加密

import time
import hashlib

# 共识tocken
base_sign = '孔敬淳'


# 生成hashlib加密串
def generate_hashlib():
    user_time = int(time.time())
    user_token = '%s%s' % (base_sign, user_time)
    # 生成hash对象
    hashobj = hashlib.sha1(user_token.encode('utf-8'))
    # 生成hash值
    a_token = hashobj.hexdigest()
    return a_token, user_time


# 验证hashlib加密串
def check_hashlib(user_hash, user_time):
    servier_token = '%s%s' % (base_sign, user_time)
    server_hash = hashlib.sha1(servier_token.encode('utf-8')).hexdigest()
    if server_hash == user_hash:
        print('认证成功')
        return True
    else:
        print('认证失败')
        return False


if __name__ == '__main__':
    u_hash, u_time = generate_hashlib()
    result = check_hashlib(u_hash, u_time)
