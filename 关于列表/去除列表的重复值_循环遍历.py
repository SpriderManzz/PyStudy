# cdoing=utf-8
list1 = [11, 22, 11, 22, 33, 44, 55, 33, 66]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print list1
print list2
