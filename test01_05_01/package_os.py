# coding:utf-8
# @Create time: 2021/3/18 11:48 上午
# @Author: KongJingchun
# @remark: OS包的使用

import os

# 获取当前文件所在的路径
current_path = os.getcwd()
print(current_path)

new_dir = 'dirtest'
# 创建新文件夹
# os.mkdir(new_dir)
# 修改文件或者文件夹名称
# os.rename('dirtest', 'new_dirtest')
# 删除空文件夹
# os.rmdir('%s/new_dirtest' % current_path)
# 删除文件夹，可以不为空
# os.removedirs('%s/new_dirtest' % current_path)
# 判断文件或者路径是否存在
# print(os.path.exists('%s/dirtest' % current_path))
# 判断是否是路径
# print(os.path.isdir('%s/dirtest' % current_path))
# 判断是否是绝对路径
# print(os.path.isabs('%s/dirtest' % current_path))
# 判断是否是文件
# print(os.path.isfile('%s/test.py' % current_path))
# join链接路径
# print(os.path.join(current_path, new_dir))
# 切割最后一层路径
# print(os.path.split(current_path))
