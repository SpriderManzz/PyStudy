# coding=utf-8
import time

# time.time()是获取从1970年到现在的时间，单位是秒
print time.time()

print time.localtime()

# 格式化时间按照2018-01-02 20:18:50的格式打印出来
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
