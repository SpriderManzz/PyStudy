# -*- coding: utf-8 -*-
'''print ("———————----------------------------字符串拼接和输入 ——————————————————————")
A = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
A += "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n:"
name = input(A)
print name

name1 = input("再次输入")
print name1
'''

'''
print ("———————---------------------------把字符串转换成数值 ——————————————————————")
age = input("请输入你的年龄:\n")
age = int(age)
if age >= 18:
    print ("你已经成年")
else:
    print ("你还未成年")
'''

'''
print ("———————---------------------------判断一个数是奇数还是偶数 ——————————————————————")
age = raw_input("请输入一个数据：\n")
age = int(age)
if age % 2 == 0:
    print ("你输入的是偶数")
else:
    print ("你输入的是奇数")
'''

'''
print ("———————---------------------------while 循环——————————————————————")
num = 1
while num <= 5:
    print (num)
    num += 1
'''

'''

'''

'''
print ("———————--------------------------让用户选择退出——————————————————————")
prompt = "\n请输入内容:"
prompt += "\n输入quit时会退出"
message = ""
while message != 'quit':
    message = input(prompt)
    print (message)
'''

'''
print ("———————--------------------------循环输出单数——————————————————————")
print ("———----continue的意思 满足continnue就不执行下面的语句并返回循环的开头—————————————--—————")

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print (num)
'''

'''
print ("———————--------------------------循环删除列表中所有特定元素——————————————————————")
pets = ['cat', 'dog', 'monkey', 'cat', 'pig', 'dog']
print (pets)
while 'cat' in pets:
    pets.remove('cat')
print ('删除cat之后就没cat了：')
print ( pets)
'''
'''
print("————--------------------------把变量存进去字段，定义标志用来控制循环与否，—————————————") 
# 定义一个空的字段
responses = {}
# 设置一个标志，指出循环是否继续
polling_active = True
while polling_active:
    # 提示输入着输入调查者的名字和回答
    name = raw_input("\n你的名字是什么:")
    response = raw_input("\n你喜欢什么山:")

    # 将回到存到字典里面
    responses[name] = response
    # 看看使用还有要参与
    repeat = raw_input("\n你喜欢要帮别人回答？Y/N")
    if repeat == 'N':
        polling_active = False

print("调查结果如下：")
for nem,response in responses.items():
    print (name + "喜欢爬" + response +".")
'''









