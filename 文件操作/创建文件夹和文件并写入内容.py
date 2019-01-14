# coding=utf-8
import os
mulu = '图片'
if not os.path.isdir(mulu):
    os.mkdir(mulu)
img = os.path.join(mulu, '222.txt')
print(img)
print(type(img))
with open(img, 'w') as f:
    f.write('张三\n')
    f.write('李四\n')

