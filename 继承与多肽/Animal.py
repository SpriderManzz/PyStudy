# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print('Animal is running...')

class Cat(Animal):
    def run(self):
        print ("Cat is running ")


class Dog(Animal):
    def run(self):
        print ("Dog is running ")

    def eat(self):
        print ("Dog is eating")



animal = Animal()
cat = Cat()
dog = Dog()


dog.run()
dog.eat()
cat.run()

