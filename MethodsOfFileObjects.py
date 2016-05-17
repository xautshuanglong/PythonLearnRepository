# coding:utf-8

# 文件操作

fileObj = open('file.txt','r')
lineCnt = 0
for line in fileObj.readlines():
	lineCnt += 1
	print line,
fileObj.close()
str = ('the number of lines:',lineCnt)
print str[1]
