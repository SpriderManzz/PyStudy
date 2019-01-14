# -*- coding: utf-8 -*-
# 一个类可以继承另外一个类，被继承的类称为父类，子类获得父类的所有属性和方法，子类还可以定义自己的属性和方法
class Car(object):
    def __init__(self, make, model, year):
        """ 描述汽车类的尝试"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def full(self):
        """ 返回完整的信息"""
        full_message = self.make.title() + " " + self.model + " " + str(self.year)
        return full_message

    def red_odometer(self):
        """打印汽车的里程消息"""
        print ("车开了"+str(self.odometer_reading) + "公里了")

    def update_odometer(self, mileage):
        """
        调用方法改变值
        """
        self.odometer_reading = mileage

    def fill_fly(self):
        print ("车会飞")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        '''初始化父类的属性'''
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = 30

    def describe_battery(self):
        '''
        给子类定义属性和方法
        '''
        print ("电动车的电瓶容量为" + str(self.battery) + "小时" )

    def fill_fly(self):               # 重写了父类的方法，子类方法名必须要与父类相同，调用该方法时就不会调用父类的方法了
        print ("车才不会飞")



electricA = ElectricCar('爱玛士', 'Q7', '2015')
print (electricA.full())
electricA.describe_battery()
electricA.fill_fly()
