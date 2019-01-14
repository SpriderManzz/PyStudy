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


dog_A = Dog('小白',6)
dog_A.sit()

dog_A.type2 = '第二属性还是狗'    # 实例变量绑定属性
print dog_A.type2

