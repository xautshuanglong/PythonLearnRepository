# encoding:utf-8

print("============= Class Learn =============")

# from TestClass import MyClass
from BaseClass import BaseClass
from DerivedClass import DerivedClass

"""
a = MyClass(1,"Shuang")
a.toString()

b = MyClass(2,"Long")
b.toString()
"""

base = BaseClass(110,'Shuang')
base.toString()
base.testFunc()

derived = DerivedClass(111,'Long')
derived.toString()
derived.testFunc()
derived.newFunc()
