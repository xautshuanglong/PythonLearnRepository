# encoding:utf-8
print("log4py configuration testing")
import logging,logging.config

# 通过配置文件 [log4py.conf] 设置 log4py 的属性
logging.config.fileConfig("log4py.conf")
log = logging.getLogger()
#log1 = logging.getLogger("stream")
#log2 = logging.getLogger("tempFile")
#log3 = logging.getLogger("rotateFile")
log.setLevel(logging.NOTSET)

log.debug("Debug Testing ...")
log.info("Info Testing ...")
log.warn("Warn Testing ...")
log.warning("Warinig Testing ...")
log.error("Error Testing ...")
log.fatal("Fatal Testing ...")
log.critical("Critical Testing ...")

logging.shutdown()
