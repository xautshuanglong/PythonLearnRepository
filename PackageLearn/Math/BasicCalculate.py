# encoding:utf-8

from .  import ComplexCalculate

testValue = 9999

def add(x,y):
    return x+y

def minus(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return float(x)/float(y)

if(__name__ == "__main__"):
    import sys
    if(len(sys.argv) < 3 ):
        print "argument is not enough..."
    elif(len(sys.argv) > 3):
        print "the rest arguments will be ignore.."
    else:
        print sys.argv[1],"+",sys.argv[2],"=",add(int(sys.argv[1]),int(sys.argv[2]))
        print sys.argv[1],"-",sys.argv[2],"=",minus(int(sys.argv[1]),int(sys.argv[2]))
        print sys.argv[1],"*",sys.argv[2],"=",multiply(int(sys.argv[1]),int(sys.argv[2]))
        print sys.argv[1],"/",sys.argv[2],"=",divide(float(sys.argv[1]),float(sys.argv[2]))
