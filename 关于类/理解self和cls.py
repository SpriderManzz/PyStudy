# coding=utf-8
class A(object):
    def foo1(self):
        print "Hello", self

    @staticmethod
    def foo2():
        print "hello"

    @classmethod
    def foo3(cls):
        print "hello", cls


a = A()
print "这是实例a",a
a.foo1()  # 最常见的调用方式，但与下面的方式相同
A.foo1(a)  # 这里传入实例a，相当于普通方法的self
A.foo2()  # 这里，由于静态方法没有参数，故可以不传东西
A.foo3()  # 这里，由于是类方法，因此，它的第一个参数为类本身。


A  # 可以看到，直接输入A，与上面那种调用返回同样的信息。
