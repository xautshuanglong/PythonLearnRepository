# encoding:utf-8
print("log4py testing")
import logging
import logging.config

# StreamHandler == ConsoleAppender,输出到流，控制台调试
streamFmt = logging.Formatter('%(name)s %(asctime)s %(message)s')
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
