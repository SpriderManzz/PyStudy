# -*- coding: utf-8 -*-
print ("----------------------------------------    字典   键  值——————————————————————")
#             dog 是键    xiaotugou 是值

animal = {'dog': 'xiaotugou', 'cat': 'jumao'}            # 定义了一个字典,然后输出
print (animal['dog'])
print (animal['cat'])

car = {}
car['bus1'] = 200                  # 定义了一个空字典,然后赋值进去
car['bus2'] = 500
print car

animal = {'dog':'xiaotugou', 'cat': 'jumao'}
print ('没改之前是' + animal['dog'] )
animal['dog'] = 'datugou'                           # 修改键值
print ('现在dog变成了' + animal['dog'] )

animal = {'dog':'xiaotugou', 'cat': 'jumao'}
del animal['dog']                                       # 删除键值
print animal


print ("——————————————————       字母顺序遍历字典的 键      —————————————————————")
study = {
    'tom': 'java',
    'jason': 'c',
    'jack': 'python'
    }
print ('学习的人有：')
for name in sorted(study.keys()):
    print (name.title())


print ("———————————————       遍历字典的 值   并去除相同的值&& 字母顺序遍历  ————————————————————")
study = {
    'tom': 'java',
    'jason': 'c',
    'jack': 'python',
    'jon': 'python'
    }
print ('学习语言有：')
for name in sorted(set(study.values())):
    print (name.title())


print ("——————————————————       遍历字典的 键-值对      —————————————————————")
study = {
    'tom': 'java',
    'jason': 'c',
    'jack': 'python'
    }
for name, langue in study.items():
    print ('\n ' + name.title() + '正在学习' + langue.title())







