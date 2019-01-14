# -*- coding: utf-8 -*-
print ("--------------------------------------  list列表    --------------------------------------------------------")
list = ['runoob',786,2.23,'join',70.2]
tinylist = [123,'join']

print list                        # ['runoob',786,2.23,'join',70.2]
print list[0]                     # 'runoob'
print list[1:3]                   # [786,2.23]
print list[2:]                    # [2.23,'join',70.2]
print tinylist * 2                # [123,'join',123,'join'']
print list + tinylist             # ['runoob',786,2.23,'join',70.2,123,'join']


print ("-------------------------------------- tuple元组  不允许更新   ------------------------------------------------------")
tuple = ('runoob',786,2.23,'join',70.2)
tinytuple = (123,'join')

print tuple                     # {'runoob',786,2.23,'join',70.2}
print tuple[0]                  # 'runoob'
print tuple[1:3]                # {786,2.23,'join'}
print tuple[2:]                 # {2.23,'join',70.2}
print tinytuple * 2             # {123,'join',123,'join'}
print tuple + tinytuple         # {'runoob',786,2.23,'join',70.2,123,'join'}



print ("-------------------------------------- dictionary 字典       ----------------------------------------------")
dict = {}
dict['one'] = " this is one"
dict[2] = "this is two"
tinydict = {'name': 'join', 'code': 6734, 'dept': 'sales'}

print dict['one']                       # this is one
print dict[2]                           # this is two
print tinydict                          # {'name': 'join', 'code': 6734, 'dept': 'sales'}
print tinydict.keys()                   # ['name','code','dept']
print tinydict.values()                 # ['join','6734','sales'    ]
