# -*- coding: utf-8 -*-
'''
print ("--------------------------      函数可以多次调用   关键字实参     ---------------------------------------------------")


def car (car_type, car_name):   # 形参
    """ 这是文档字符串"""
    print ("我有一款" + car_type)
    print (car_type + "的名字是" + car_name)


car( car_type='SUV', car_name='RAV4')      # 实参
car(car_name='路虎',car_type='越野')
'''

'''
print ("--------------------------       默认值     ---------------------------------------------------")
print ("'使用默认值必需先把形参中无默认值的写在前面")


def car (car_name,car_type='SUV'):   # 形参
    """ 这是文档字符串"""
    print ("我有一款" + car_type)
    print (car_type + "的名字是" + car_name)


car(car_name='RAV4')      # 实参
car('RAV5')   # 只给值
'''

'''
print ("--------------------------       返回值     ---------------------------------------------------")


def name(first_name, last_name):
    """ 返回完整的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()


message = name('jack', 'zhou')            # 调用返回值的函数时，需提供一个变量，用于存储返回的值。
print (message)
'''

'''
print ("--------------------------       让实参变成可选的    ---------------------------------------------------")


def name(first_name, last_name, middle_name=''):
    """ 返回完整的姓名"""
    if middle_name:
        full_name = first_name + " " + last_name
    else:
        full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()


message = name('jack', 'lee')
print (message)

message = name('jack', 'lee', 'tom')
print (message)
'''

'''
print ("--------------------------       返回字典 ,并且实参可选  ---------------------------------------------------")

def person(first_name, last_name, age=''):
    """ 返回一个字典，里面包含一个人的姓名"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age                         
    return person
message = person('xiao', 'ming',)
print (message)
'''

'''
print ("--------------------------       函数结合while循环使用  ---------------------------------------------------")
def name(first_name, last_name):
    """ 函数结合while循环使用"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print ("\n请输入你的姓名")
    print ("输入q退出")

    f_name = raw_input("姓：")
    if f_name == 'q':
        break

    l_name = raw_input("名：")
    if l_name == 'q':
        break

    message = name(f_name, l_name, )
    print ("hello: " + message + "!")
'''


'''
print ("--------------------------       传递列表  ---------------------------------------------------")
""" 像列表中的每个成员发出问候循环使用"""
def greet(names):
    for name in names:
        message = ("hello:" + name.title() + "!")
        print (message)


usersnames = ['tom', 'jack', 'tonty', 'jackson']
greet(usersnames)
'''

'''
print ("--------------------------       传递任意数量的实参  ---------------------------------------------------")
def make_food( *topping ):      #创了一个空的元组，并将收到的值存进去
    print ("制作奶昔使用了如下食材")
    for _topping in topping:
        print ( _topping)

make_food('苹果','香蕉','牛奶')
'''