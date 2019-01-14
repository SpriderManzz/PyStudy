# coding=utf-8
def describe_pet(animal_type, pet_name):  # 这里的animal_type, pet_name是形参
    print ("我的宠物" + animal_type + '名字叫做:' + pet_name)

describe_pet(animal_type='cat', pet_name='kity')

describe_pet(pet_name='kity',animal_type='cat')  # 位置互换也行