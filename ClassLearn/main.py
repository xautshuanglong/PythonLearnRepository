# encoding:utf-8

print("============= Class Learn =============")

from BaseClass import BaseClass
from DerivedClass import DerivedClass


from TestClass import MyClass

print "Before:",MyClass.testVar

a = MyClass(1,"Shuang")
a.toString()
MyClass.testVar = 456
print a.testVar

b = MyClass(2,"Long")
b.toString()
print b.testVar

print "After:",MyClass.testVar

"""
base = BaseClass(110,'Shuang')
base.toString()
base.testFunc()

derived = DerivedClass(111,'Long')
derived.toString()
derived.testFunc()
derived.newFunc()
"""
