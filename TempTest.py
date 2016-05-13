# encoding:utf-8

'''
import Fibo

res = Fibo.fibonacci(2000);
print "Module name:",Fibo.__name__
print res
fibo = Fibo.fibonacci
print fibo(2000)
'''
from Fibo import fibonacci

print fibonacci(200)

import Fibo
print dir(Fibo)
