<<<<<<< HEAD
# encoding:utf-8
=======
print '<================ Inside Fibo.py ===============>'
>>>>>>> 957e5dd92fc24c050425f05f3dcbca7d30dea087

def fibonacci(n):
	a,b = 0,1
	res = []
<<<<<<< HEAD
	while(a<n):
		res.append(a)
		a,b = b,a+b
	return res
=======
	print "res len = %d" % len(res)
	while(a<n):
		res.append(a)
		a,b = b,a+b
	print res

if __name__ == "__main__":
    import sys
    fibonacci(int(sys.argv[1]))
>>>>>>> 957e5dd92fc24c050425f05f3dcbca7d30dea087
