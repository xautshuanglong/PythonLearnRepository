# encoding:utf-8
print("log4py testing")
import logging
import logging.config

logging.basicConfig(level=logging.DEBUG)# 默认级别：WARNING, WARN, 30

log = logging.getLogger()
log.debug("Debug Testing ...")
log.info("Info Testing ...")
log.warn("Warn Testing ...")
log.warning("Warinig Testing ...")
log.error("Error Testing ...")
log.fatal("Fatal Testing ...")
log.critical("Critical Testing ...")
