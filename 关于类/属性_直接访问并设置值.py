# -*- coding: utf-8 -*-
class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性odometer_reading初始化默认值0

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

car_A = Car('audi', 'Q4', '2015')
print (car_A.full())

car_A.odometer_reading = 1000             # 直接访问并设置汽车属性odometer_reading


# car_A.update_odometer(2)
car_A.red_odometer()
