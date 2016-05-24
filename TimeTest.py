# coding:utf-8

import sys,time,locale

def printf(func):
	print("%s.%s(): %s" % (func.__module__,func.__name__,func()))
printf(sys.getdefaultencoding)
printf(sys.getfilesystemencoding)
printf(locale.getdefaultlocale)
printf(locale.getpreferredencoding)

timeStr = unicode('当前时间：','utf-8')
while(1):
	print timeStr+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	time.sleep(1)
