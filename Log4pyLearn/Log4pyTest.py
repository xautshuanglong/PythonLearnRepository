# encoding:utf-8
print("log4py testing")
import logging
import logging.handlers
import sys

# StreamHandler == ConsoleAppender,输出到流，控制台调试
streamFmt = logging.Formatter('[ %(levelname)-8s ] %(asctime)s %(name)s %(message)s','%H:%M:%S')
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
stream.setFormatter(streamFmt);

# FileHandler == FileAppender,输出到指定文件 [不追加，用于临时运行调试]
tempFile = logging.FileHandler("tempFile.log",'w')
tempFile.setLevel(logging.DEBUG)
tempFile.setFormatter(streamFmt)

# RotatingFileHandler = RollingFileAppender,按指定大小回滚 [追加，长期运行记录]
fileFmt = logging.Formatter('[ %(levelname)-8s ] %(asctime)s %(name)s %(message)s')# 使用默认时间格式
rotateFile = logging.handlers.RotatingFileHandler("rotateFile.log",'a',10485760,5)# 超过 10M 则分割文件，最多保留5个分割文件
rotateFile.setLevel(logging.INFO)
rotateFile.setFormatter(fileFmt)

log = logging.getLogger()
log.setLevel(logging.NOTSET)# 默认是 WARNING 级别，并且被其他 Handler 继承

log.addHandler(stream)
log.addHandler(tempFile)
log.addHandler(rotateFile)

log.debug("Debug Testing ...")
log.info("Info Testing ...")
log.warn("Warn Testing ...")
log.warning("Warinig Testing ...")
log.error("Error Testing ...")
log.fatal("Fatal Testing ...")
log.critical("Critical Testing ...")

"""
http://www.phperz.com/article/16/0120/93998.html
http://blog.csdn.net/fxjtoday/article/details/6307285
http://zeping.blog.51cto.com/6140112/1259065
http://blog.csdn.net/chosen0ne/article/details/7319306
"""
