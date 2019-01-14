# -*- coding:utf-8 -*-
class Student(object):
    def __init__(self):
        print("在创建实例时__init__方法被自动调用了")


S1 = Student()


def funb(self):
    print '这是方法'

class B():
    def __init__(self, b):
        self.b = b
    def B_fun(self):
        print ("这是类B才有的方法")

class A():
    def __init__(self, a):
        self.a = a


a1 = A(funb) # __init__参数可以传字符串，方法，类都可以看你需要

a2 = A(B)  # 如果传的类的话，那么实例a2，就没有被传入类B的方法和属性，只有当前类的所有属性和方法
# print dir(a2)

# a2.a 可以看成类B
a2.a.B_fun

