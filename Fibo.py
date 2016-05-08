print '<================ Inside Fibo.py ===============>'

def fibonacci(n):
	a,b = 0,1
	res = []
	print "res len = %d" % len(res)
	while(a<n):
		res.append(a)
		a,b = b,a+b
	print res

if __name__ == "__main__":
    import sys
    fibonacci(int(sys.argv[1]))
