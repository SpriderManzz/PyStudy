# -*- coding:utf-8 -*-

# 在类的内部，访问自己的属性和方法，都需要通过self，self就是外部对象在类内部的表示，此时可以使用p调用该方法
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def desc(self):
        print("名字%s，今年%d岁" % (self.name, self.age))
        print ("desc中的self是：%s" %self)

p1 = Person('张三', 20)
p2 = Person('李四',40)
# 调用自我介绍方法 desc方法中的self就是外部的这个p
p1.desc()
p2.desc()

print ("实例p的地址%s"%p1)
print ("实例p2的地址%s"%p2)
# 当前desc方法中的self，就是外部的那个对象p
# 如果我再定义了一个对象p2，那么p2调用desc时，desc中的self就表示p2这个对象。正所谓：谁调用，就表示谁