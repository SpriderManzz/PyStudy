# -*- coding: utf-8 -*-

print ("-----------------------------算术运算符-----------------------------------------------------------------")
a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c           # 31

c = a - b
print "2 - c 的值为：", c          # 11

c = a * b
print "3 - c 的值为：", c          # 210

c = a / b
print "4 - c 的值为：", c          # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  2

c = a % b     # 取模
print "5 - c 的值为：", c        # 1

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b   # b的幂次方
print "6 - c 的值为：", c        # 8

a = 10
b = 5
c = a // b    # 取整
print "7 - c 的值为：", c            # 2


print ("------------------------------------比较运算符-----------------------------------------------------------")

a = 21
b = 10
c = 0

if( a == b ):
    print ("1 - a 等于 b")
else:
    print ("1 - a 不等于 b")

if (a != b):
    print "2 - a 不等于 b"
else:
    print "2 - a 等于 b"

if (a <> b):
    print "3 - a 不等于 b"
else:
    print "3 - a 等于 b"

if (a < b):
    print "4 - a 小于 b"
else:
    print "4 - a 大于等于 b"

if (a > b):
    print "5 - a 大于 b"
else:
    print "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5
b = 20
if (a <= b):
    print "6 - a 小于等于 b"
else:
    print "6 - a 大于  b"

if (b >= a):
    print "7 - b 大于等于 a"
else:
    print "7 - b 小于 a"


print ("------------------------------------赋值运算符-----------------------------------------------------------")

a = 21
b = 10
c = 0

c = a + b    # 31
print "1 - c 的值为：", c

c += a      # c = c + a  52
print "2 - c 的值为：", c

c *= a       # c = c * a  1092
print "3 - c 的值为：", c

c /= a       # c = c / a 0
print "4 - c 的值为：", c

c = 2
c %= a       # c = c % a 0
print "5 - c 的值为：", c

c **= a      # c = c ** a
print "6 - c 的值为：", c

c //= a     # c = c // a
print "7 - c 的值为：", c