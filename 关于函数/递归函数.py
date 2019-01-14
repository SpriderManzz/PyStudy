# -*- coding: utf-8 -*-
print ("n的阶乘n!")
def fact(n):
    if n == 1:
        return None
    return n * fact(n-1)

print fact(1)
