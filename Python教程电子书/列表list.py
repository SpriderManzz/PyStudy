# -*- coding: utf-8 -*-
classmates = ['A','B','C']
L = ['good',123,True]
M =['Pyhon','java',['asp','php'],'C']
K =[]
print "列表classmates的元素:",classmates
print "列表L的元素:",(L)
print "列表M的元素:",(M)
print "列表K的元素:",(K)




print ("取列表M中第三个元素中的第二个元素")
print M[2][1]

print ("返回列表个数")
print len(classmates)
print len(K)

print ("头部开始用索引访问列表的元素，索引从0开始")
print classmates[0]
print classmates[1]
print classmates[2]

print ("索引也可以从尾部开始，但是索引为-1")
print classmates[-1]
print classmates[-2]
print classmates[-3]

print ("append --末尾添加元素'D'")
classmates.append('D')
print classmates

print ("pop --末尾删除元素'C'")
classmates.pop()
print classmates


print ("insert --插入元素'E'到指定位置")
classmates.insert(1,'E')
print classmates

print ("修改指定元素'E'的值")
classmates[1] = 'E1'
print classmates

print ("pop--删除指定位置的元素'E'")
classmates.pop(1)
print classmates


print ("pop删除元素'E'----返回元素")
pop_list = ['A','B','C','D','E']
is_poped = pop_list.pop(-1)
print is_poped
print pop_list


print ("remove删除元素'E'--返回列表,不返回元素None")
remove_list=['A','B','C','D','E']
is_removeed = remove_list.remove('E')
print is_removeed
print remove_list


print ("del删除元素'E'----不返回值")
del_list=['A','B','C','D','E']
del del_list[-1]
print del_list






