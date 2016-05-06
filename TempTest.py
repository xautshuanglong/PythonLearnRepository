print('The range() function')
print range(5,10)

def fibonacci(n):
	a,b = 0,1
	res = []
	print "res len = %d" % len(res)
	while(a<n):
		res.append(a)
		a,b = b,a+b
	print res
fibonacci(2000);

print '<======================================>'
mat = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
print [[row[i] for row in mat] for i in range(0,3)]

a = range(1,10)
b = xrange(1,10)

print 'a = ',a,'  type(a)=',type(a)
print 'b = ',b,'  type(b)=',type(b)
print b[2],b[1]

list = ['value2','value1','value0']
for value in sorted(set(list)):
	print value
