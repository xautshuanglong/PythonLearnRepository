# encoding:utf-8

def fibonacci(n):
	a,b = 0,1
	res = []
	while(a<n):
		res.append(a)
		a,b = b,a+b
	return res
