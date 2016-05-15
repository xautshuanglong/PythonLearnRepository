# encoding:utf-8

'''
import Fibo

res = Fibo.fibonacci(2000);
print "Module name:",Fibo.__name__
print res
fibo = Fibo.fibonacci
print fibo(2000)
'''

'''
from Fibo import fibonacci
print fibonacci(200)

import Fibo
print dir(Fibo)
'''

'''
import PackageLearn.Math.BasicCalculate
print PackageLearn.Math.BasicCalculate.add(3,2)
print PackageLearn.Math.BasicCalculate.minus(3,2)
print PackageLearn.Math.BasicCalculate.multiply(3,2)
print PackageLearn.Math.BasicCalculate.divide(3,2)
'''

'''
from PackageLearn.Math.BasicCalculate import add,minus,multiply,divide
print add(3,2)
print minus(3,2)
print multiply(3,2)
print divide(3,2)
'''


from PackageLearn.Math import *
from PackageLearn import Math
print BasicCalculate.add(3,2)
print BasicCalculate.minus(3,2)
print BasicCalculate.multiply(3,2)
print BasicCalculate.divide(3,2)
print BasicCalculate.testValue
