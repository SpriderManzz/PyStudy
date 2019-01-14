# -*- coding: utf-8 -*-
print ("创建小狗类,并且创建了实例dog_A,dog_B,然后通过实例调用类中的方法")
class Dog(object):
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        self.type = 'dog'

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print (self.name + "已经坐下了")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print (self.name + "已经打滚了\n")

dog_A = Dog('while', 6)                            # 根据类创建了一个实例dog_A
print ("小狗名字叫：" + dog_A.name.title() + "")
print ("小狗年龄为：" + str(dog_A.age) + "岁")
dog_A.sit()
dog_A.roll_over()

dog_B = Dog('tom', 3)                            # 根据类创建了一个实例dog_B
print ("小狗名字叫：" + dog_B.name.title() + "")
print ("小狗年龄为：" + str(dog_B.age) + "岁")
dog_B.sit()
dog_B.roll_over()

