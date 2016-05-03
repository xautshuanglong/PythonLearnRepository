# encoding:utf-8
print("log4py testing")
import logging
import logging.config

# StreamHandler == ConsoleAppender,输出到流，控制台调试
streamFmt = logging.Formatter('[ %(levelname)-8s ] %(asctime)s %(name)s %(message)s')
stream = logging.StreamHandler()
stream.setLevel(logging.DEBUG)
stream.setFormatter(streamFmt);

log = logging.getLogger()
log.addHandler(stream)

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
