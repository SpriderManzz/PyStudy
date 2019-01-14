# coding=utf-8
from name_function import get_formatted_name

print ("---------------请按q退出程序----------------------")
while True:
    first = raw_input("请输入你的姓:")
    if first == 'q':
        break
    last = raw_input("请输入你的名字:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print ("你输入的姓名是:"+ formatted_name + '\n')