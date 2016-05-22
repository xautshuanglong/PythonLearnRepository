
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

"""
string = "Helo,world."
strTemp = "--Shuanglong"
print string
print str(string)
print repr(string)
print string.ljust(5)[2:7],strTemp.ljust(5)[2:7]
print string.rjust(5),strTemp.rjust(5)
"""
"""
num = 100
print "%d to hex is %x" %(num, num)
print "%d to hex is %X" %(num, num)
print "%d to hex is %#x" %(num, num)
print "%d to hex is %#X" %(num, num) 

f = 3.1415926
print "value of f is: %.4f" % f

lists = [{"name":"name1", "age":27}, {"name":"name2", "age":28}, {"name":"name3", "age":26}]
print "name: %10s, age: %10d" % (lists[0]["name"], lists[0]["age"])
print "name: %-10s, age: %-10d" % (lists[1]["name"], lists[1]["age"])
print "name: %*s, age: %0*d" % (10, lists[2]["name"], 10, lists[2]["age"])

for item in lists:
    print "%(name)s is %(age)d years old" % item
"""

table = {'key1':111,'key2':222,'key3':333}
print('key1:{key1:d},key2:{key2:d},key3:{key3:d}'.format(**table))
print('key1:{key1:#x},key2:{key2:#x},key3:{key3:d}'.format(**table))
# 位置参数
print "{0} is {1} years old".format("Wilber", 28)
print "{} is {} years old".format("Wilber", 28)
print "Hi, {0}! {0} is {1} years old".format("Wilber", 28)

# 关键字参数
print "{name} is {age} years old".format(name = "Wilber", age = 28)

# 下标参数
li = ["Wilber", 28]
print "{0[0]} is {0[1]} years old".format(li)

# 填充与对齐
# ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print '{:>8}'.format('3.14')
print '{:<8}'.format('3.14')
print '{:^8}'.format('3.14')
print '{:0>8}'.format('3.14')
print '{:a>8}'.format('3.14')

# 浮点数精度
print '{:.4f}'.format(3.1415926)
print '{:0>10.4f}'.format(3.1415926)

# 进制
# b、d、o、x分别是二进制、十进制、八进制、十六进制
print '{:b}'.format(11)
print '{:d}'.format(11)
print '{:o}'.format(11)
print '{:x}'.format(11)
print '{:#x}'.format(11)
print '{:#X}'.format(11)

# 千位分隔符
print '{:,}'.format(1570000000)
