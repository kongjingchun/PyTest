# coding:utf-8
# @Create time: 2021/3/18 3:08 下午
# @Author: KongJingchun
# @remark: sys包的使用

import sys

modules = sys.modules
# 获取启动python时启动的模块
# print(modules)
path = sys.path
print(path)
# 获取默认的编码格式
code = sys.getdefaultencoding()
print(code )
# 获取电脑的系统
print(sys.platform)
# 获取python版本
print(sys.version)

# 通过外部进行传参
print(sys.argv)
# 退出程序
sys.exit(1)

