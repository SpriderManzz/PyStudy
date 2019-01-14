# coding=utf-8
class Dog(object):
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        self.type = 'dog'  # type属性直接赋值

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print (self.name + "已经坐下了")

    def update_type(self,new_type):
        self.type = new_type

dog_A = Dog('小白',6)
dog_A.update_type('peg')
print dog_A.type
dog_A.sit()

