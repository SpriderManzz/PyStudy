# -*- coding: utf-8 -*-
classmates = ('A','B','C')

print "元组classmates的元素:",classmates

print ("头部开始用索引访问元组的元素，索引从0开始")
print classmates[0]
print classmates[1]
print classmates[2]

print ("索引也可以从尾部开始，但是索引为-1")
print classmates[-1]
print classmates[-2]
print classmates[-3]

print ("定义空的元组")
K = ()
print K

print ("定义只有1个元素的元组必须加,不然就是数学公式了")
K1= (1,)
print K1

print ("元组里面有列表")
T_t = ('A','B','C',['E','F','G','H'],'H')
print T_t

print '修改元组中列表元素'
T_t[3][0] ='E1'
print '访问元组中列表元素',T_t[3][0]

