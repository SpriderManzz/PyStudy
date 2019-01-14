# -*- coding: utf-8 -*-
print ("-----------字符串转化为整形")
r = "123"
print "一开始123为：",type(r)
r = eval(r)
print '然后变成了：', type(r)


print ("-----------整形转化为字符串")
r = 123
print "一开始123为：",type(r)
r = str(r)
print '然后变成了：', type(r)

print ("-----------实数取整")
r = 123.456789
print "一开始123.456789为：",type(r)
r = int(r)
print '然后变成了：', type(r),r



