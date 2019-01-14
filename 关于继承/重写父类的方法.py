# coding=utf-8
class Animal(object):
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def eat(self):
        print (self.name + "会进食")

    def sleep(self):
        print (self.name + "会睡觉")

    def swim(self):
        print (self.name + "会游泳")

class Dog(Animal):
    def __init__(self, name, age):
        """初始化父类的属性"""
        super(Dog, self).__init__(name, age)
        self.bite_food = '骨头'

    def like_bite(self):
        print (self.name + "喜欢啃" + self.bite_food)

    def swim(self):  # 重写了父类的方法
        print (self.name + "不喜欢游泳")


dog = Dog('小白', 3)
dog.eat()
dog.like_bite()
dog.swim()




