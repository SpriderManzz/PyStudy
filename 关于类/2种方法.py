# coding=utf-8
class Dog():
    def __init__(self, name):
        self.name = name

    def pr(self):
        print "名字是" + self.name

dog = Dog("小黄") # 本质调用的是__init__方法函数
dog.pr()
Dog.pr(dog)
