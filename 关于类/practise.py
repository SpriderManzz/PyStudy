class A(object):
    @classmethod
    def fn1(cls):
        print (cls)
    def fn2(self):
        print(self)
    def fn3(self):
        print(self)
g = A()
print g, A
g.fn1() # 即使是写成g.fn1()  也等于A.fan1()
g.fn2()
g.fn3()

