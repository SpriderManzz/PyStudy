# -*- coding: utf-8 -*-
if 2:
    print('只要条件不是非零数值、非空字符串、非空list等就判断为true')


print ("用循环显示列表的元素")
num =['A','B','C','D']
for i in num:
    print i

print ("用循环计算0到100的和")
sum =0
for i in range(101):
    sum = sum + i
print sum



print ("用循环计算1到100的奇数和")
sum = 0
n = 99
while n > 0:
    #print n,'进来循环进来的值'
    sum = sum + n
    #print sum, '加上上一次累加的和'
    n = n - 2
print sum

print ("用循环计算1到100的偶数和")
sum = 0
n = 10
while n > 0:
    print n,'进来循环进来的值'
    sum = sum + n
    # print sum, '加上上一次累加的和'
    n = n - 2
print sum