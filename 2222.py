# -*- coding: utf-8 -*-
print ("创建小狗类,并且创建了实例dog_A,dog_B,然后通过实例调用类中的方法")
class Dog(object):
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.age = age
        self.name = name
        self.type = 'dog'

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print (self.name + "已经坐下了")

    def update_type(self, type):
        self.type = type


dog_A = Dog('while', 6)                            # 根据类创建了一个实例dog_A
print ("小狗年龄为：" + str(dog_A.age) + "岁")
dog_A.sit()
dog_A.update_type('pet')
print dog_A.type



