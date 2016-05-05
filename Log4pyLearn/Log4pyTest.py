# encoding:utf-8
print("log4py testing")
import logging,logging.handlers
import sys

# StreamHandler == ConsoleAppender,输出到流，控制台调试
streamFmt = logging.Formatter('[ %(levelname)-8s ] %(asctime)s.%(msecs)d %(name)s %(message)s','%H:%M:%S')
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

#Informs the logging system to perform an orderly shutdown by flushing and closing all handlers. This should be called at application exit and no further use of the logging system should be made after this call.
logging.shutdown()
