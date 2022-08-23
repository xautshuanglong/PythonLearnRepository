'''
Author: Shuanglong xjshuanglong@126.com
Date: 2022-08-23 23:08:56
LastEditors: Shuanglong xjshuanglong@126.com
LastEditTime: 2022-08-23 23:13:37
FilePath: \PythonLearnRepository\TimeTest.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
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
	print(timeStr+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
	time.sleep(1)
