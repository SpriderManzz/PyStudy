# coding=utf-8
import os

# 返回当前文件夹的绝对路径
print os.path.abspath('.')

# 获取项目根目录的相对路径
print os.path.dirname(os.path.abspath('.'))

print os.path.dirname(os.getcwd())