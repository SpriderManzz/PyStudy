# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get__gender(self):
        return self.__gender

    def set__gender(self,gender):
        self.__gender = gender

bart = Student('Bart', 'male')

if bart.get__gender() != 'male':
    print('测试失败!')
else:
    bart.set__gender('female')   # 这部已经改变了 原先实例的male，变成了female
    if bart.get__gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
