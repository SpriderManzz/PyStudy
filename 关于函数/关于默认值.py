# coding=utf-8
def describe_pet(pet_name, animal_type='cat'):  #因为Python会把函数调用认为是位置实参，所以默认值放后面
    print ("我的宠物" + animal_type + '名字叫做:' + pet_name)

describe_pet(pet_name='kity',animal_type='cat')
describe_pet(pet_name='kity') # 可以省略成这个样子
describe_pet('kity')# 可以省略成这个样子

describe_pet(animal_type='dog',pet_name='lolo') #也可以这样调用换成其他