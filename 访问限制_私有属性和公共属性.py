# -*- coding: utf-8 -*-
print ("在class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样就隐藏了内部的复杂逻辑")
class Student(object):
    def __init__(self, name, score, age):
        self.name = name         # 没设置成私有变量
        self.__score = score     # 设置成私有变量
        self.__age = age         # 设置成私有变量

    def get_score(self):        # 写这个为了让外部代码要获取私有变量__score的值
        return self.__score

    def set_age(self, age):     # 写这个为了能让外部改变私有变量__age的值
        self.__age = age

    def get_age(self):        # 写这个为了能让外部获取私有变量__age的值
        return self.__age

    # def print_score(self):               ?????
    #     print ("%s" % self.__score)      ?????

lisa = Student('lisa','A,','18')   # 一个lias实例

print ('查看对象lias的属性：%s'% lisa.__dict__)

lisa.set_age('20')
print ('直接访问变量name的值：%s'% lisa.name)              # 因为name不是私有变量，所以可以被调用
print ('通过访问方法get_score()获取私自变量__score的值：%s'% lisa.get_score())
print ('通过访问方法get_age()来访问被外部代码调用get_age()改变值的私自变量__ge %s'% lisa.get_age())    # 外部代码获取私有变量__score
