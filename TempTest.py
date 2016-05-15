
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

'''
from PackageLearn.Math import *

print BasicCalculate.add(3,2)
print BasicCalculate.minus(3,2)
print BasicCalculate.multiply(3,2)
print BasicCalculate.divide(3,2)
print BasicCalculate.testValue

for x in range(1,6):
	print  repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4)

for x in range(1,6):
	print '{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x)
'''

string = "Helo,world."
strTemp = "--Shuanglong"
print string
print str(string)
print repr(string)
print string.ljust(5)[2:7],strTemp.ljust(5)[2:7]
print string.rjust(5),strTemp.rjust(5)
