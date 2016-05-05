print('The range() function')
print range(5,10)

def fibonacci(n):
	a,b = 0,1
	res = []
	print "res len = %d" % len(res)
	whil(a<n):
		res.append(a)
		a,b = b,a+b
	print res
fibonacci(2000)
