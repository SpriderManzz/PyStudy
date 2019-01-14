# -*- coding: utf-8 -*-
def f1(n):
    if n > 18:
        return '成年人'
    if n > 50:
        return '中年人'
    return
print f1(70)   # 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。  所以不输出中年人
print f1(1)    # return None 可以简写成return


