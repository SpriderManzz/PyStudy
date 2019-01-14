# -*- coding: utf-8 -*-
class Car(object):
    def __init__(self, newWheelNum, newColor, brand):
        self.wheelNum = newWheelNum
        self.color = newColor
        self.brand = brand

    def move(self):
        print('车在跑，目标:夏威夷')
    def desc_brand(self):
        print ("车的牌子是%s" %self.brand)

BMW = Car(4, 'green','宝马')

BMW.desc_brand()
print('车的颜色为:%s' %BMW.color)
print('车轮子数量为:%d'% BMW.wheelNum)
print("车的颜色%s，轮子的个数为%d个" %(BMW.color, BMW.wheelNum))