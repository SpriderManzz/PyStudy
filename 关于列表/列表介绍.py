# -*- coding: utf-8 -*-
# 列表是一系列按特定顺序排列的元素组成可以随时添加和删除其中的元素
# 索引正序从0开始，倒叙从-1开始



age = ['20', '21', '22', '23', '24', '25']
age[0] = 20.5   # 修改列表元素20为20.5
age.append(26)  # 列表末尾增加新元素26
del age[-1]     # 删除列表的元素
print (age)



age = ['20', '21', '22', '23', '24', '25']
print (age)
age.insert(3, '22.5')                           # 列表第3哪里插入元素22.5，后面的要往右挪一位
print (age)


now_age = age.pop()
print ("my age is" + now_age)                  # 删除（弹出最后一个元素）或者-1 -2 也行 弹出后还能继续用该元素


age = ['20', '21', '22', '23', '24', '25']
print (age)
remove_age = '25'
age.remove(remove_age)  # 通过元素的值来删除，删除后还能用该元素
print age
print ("刚刚删除了"+remove_age)


cars = ['audi', 'bwm ', 'toyota', 'subrau']
cars.sort()                                  # 前提是列表是小写 按元素的字母顺序排列，永久改变
print cars

cars = ['audi', 'bwm ', 'toyota', 'subrau']
cars.sort(reverse=True)                      # 前提是列表是小写 按元素的字母的刀序排列，永久改
print cars




cars = ['audi', 'bwm ', 'toyota', 'subrau']
len = cars.__len__()                           # 计算长度
print len

cars = ['audi', 'bwm ', 'toyota', 'subrau']
for car in cars:                              # 循环打印出cars列表的值
    print car

for vv in range(1, 6):                      # 生成一系列 只会打印出1到5
    print vv

message = list(range(1, 12, 2))             # 从2开始然后不断加2
print (message)

A = []
for a in range(1, 11):
    A.append(a**2)                          # 输出1~10的平方
print A


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print min(A)
print max(A)                              # 求最值和平均值
print sum(A)

# 切片   处理列表的部分元素
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]       # 因为输出也是列表所以只去前3个数字
print (A[0:3])

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = A[:]                                 # 复制一个新列表
print A
print B

print ("----------------------------------------       元组dimension      ——————————————————————")
        # 不可以改变的列表称为元组
A = (10, 20)
print (A[0])
print (A[1])


A = (20, 30)
for a in A:                                # 循环输出元组元素
    print a

A = (40, 50)
A = (50, 60)
print A

