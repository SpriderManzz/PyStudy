# -*- coding: utf-8 -*-

# 定义了一个类Dog
class Dog(object):
    def __init__(self):
        print self
        self.name = '小白'

    def sit(self):
        print (self.name + "已经坐下了")

# 创建一个类Dog的实例
dog = Dog()
dog.sit()






print ("---------------------------------------------------------------------------------------------")
print dog  # <__main__.Dog object at 0x0000000002329908> --dog是类Dog的对象在物理地址0x0000000002329908
print Dog




