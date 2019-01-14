# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name,score):
        self.__name = name       # 设置成私有变量
        self.__score = score     # 设置成私有变量

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):         # 写这个为了能让外部访问
        return self.__name

    def get_score(self):        # 写这个为了能让外部访问
        return self.__score

    def ste_score(self, score):  # 写这个为了能让外部改变score的值
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 一个lisa实例
lisa = Student('lisa','20')

print (" -----------------------外部访问私有变量  self.__name 、self.__score-------------------------------------")
print (lisa.get_name(), lisa.get_score())


print (" -----------------------外部改变变量score的值-------------------------------------")
lisa.__score = 30
#print (lisa.get_score())
print (lisa.__score)

