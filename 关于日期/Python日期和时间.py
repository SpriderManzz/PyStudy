# -*- coding: utf-8 -*-
import time

print '当前时间戳为:', time.time()    # time.time()获取的是从1970年到现在的间隔，单位是秒
print '本地时间', time.localtime()    # 输出本地时间
print '格式化时间成', time.strftime("%Y-%m-%d %H:%M:%S,", time.localtime()) # 格式为 2017-04-15 13:46:32

