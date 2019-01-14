# coding=utf-8
class Dog(object):
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        self.type = 'dog'

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print (self.name + "已经坐下了")

dog_A = Dog('小白',6)
dog_A.type = 'pet' # 修改type属性为pet
dog_A.sit()
print dog_A.type
