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
        self.dog_food = '狗粮'
        self.dogdetail = Dogdetail(name) # 每次创建 Dog的实例时都会创建一个Dogdetail类的实例

    def like_bite(self):
        print (self.name + "喜欢啃" + self.bite_food)

    def swim(self):
        print (self.name + "不喜欢游泳")

    def dog_like_food(self):
        print (self.name + "喜欢吃" + self.dog_food)


class Dogdetail():     # 定义了一个Dogdetail类，用来存放Dog类的部分具体性信息
    def __init__(self, name):
        self.dog_toy = '飞碟'
        self.name = name   # 如果不传过来，那么这个Dogdetail的实例就不会有name的属性

    def dog_like_toy(self):
        print (self.name + "喜欢玩" + self.dog_toy)


dog = Dog('小白', 3)
dog.eat()
dog.like_bite()
dog.swim()
dog.dog_like_food()

dog.dogdetail.dog_like_toy() # 所以Dog类的实例dog要实现dog_like_toy的方法的话就要加上dogdetail
                             # 因为dog_like_toy方法是Dogdetail类的实例