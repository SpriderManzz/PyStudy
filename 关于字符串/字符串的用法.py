# -*- coding: utf-8 -*-
# 字符串用法

message = 'hello word'
first_name = "Michael"
last_name = "Jackson"

print ('以首字符大写显示每个单词.title():%s'% message.title())  # 以首字符大写显示每个单词
print message.upper()    # 字符串变成大写
print message.lower()    # 字符串变成小写
print ("abcd\tefgh")     # 在字符串中加制表符   制表符等于4个空格
print ("\nabcd")         # 在字符串中加换行符

a = " hello1"
print a.lstrip()         # 去掉字符串前部的空格

b = "hello2 "
print b.rstrip()         # 去掉字符串尾段的空格

c = " hello3 "
print c.strip()           # 去掉字符串两端的空格

print 2 ** 3             # 表示2的3次方

print (2+3)*4            # 先算括号的再算乘法

print 3 / 2              # 要是想变成1.5,至少要保值一个操作数为浮点型
print 3.0 / 2


print first_name + " " + "前面的是加空格这里是加文字" + last_name
print (message)
print message.title()
print "AAA"
