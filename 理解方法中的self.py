# -*- coding:utf-8 -*-
print ("------------------------类中所有方法里的self都是指向实例的引用------------------------------------------------")
class Student(object):
    def __init__(self1, name):
        self1.name = name
        print ("__int__方法中self1的地址: %s"% self1)

    def f1(self2):
        print("类中方法f1中self2的地址: %s"% self2)

    def f2(self3):
        print("类中方法f1中self3的地址: %s"% self3)

s1 = Student('学生s1')

print ("Student类的地址: %s"% Student)

print ("实例s1的地址：%s"% s1)
s1.f1()
s1.f2()
# print ("实例s1的属性值")
print ('学生s1的名字:%s'% s1.name)


