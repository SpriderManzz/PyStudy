# -*- coding: utf-8 -*-
print ("----------------------------------------      if语句  ——————————————————————")
# 值为Ture 或者False的表达式称为条件测试
cars = ['audi', 'bwm', 'toyota', 'subaru']
for car in cars:
    if car == 'bwm':
        print (car.upper())                          # 如果遇到bwm就大写输出，遇到其他就首字母大写输出
    else:
        print (car.title())

A = "10"
B = "20"                                            # 判断2个值是否不相等
if A != B:
    print ("因为10不等于20，所以执行了这个语句")


cars = ['audi', 'bwm', 'toyota', 'subaru']
x1 = 'bwm' in cars                                # 判断制定值是否在列表中
print x1
x2 = 'haha' not in cars
print x2


age = 12
if age<4:
    print ("小于4岁")
elif age<12:
    print ("小于12岁")
else:
    print ("66")

cars = []
if cars:
    for car in cars:
        print (cars)                        # 判断是否为空表
else:
    print ("没有车")

