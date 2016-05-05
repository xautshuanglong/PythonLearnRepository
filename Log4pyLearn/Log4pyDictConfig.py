# encoding:utf-8

import logging,logging.config

print("log4py dictionary configuration")

LOG_DICT= {
	'version':1,
	'loggers':{
		'root':{
			'level':'DEBUG',
			'handlers':['streamHandler','fileHandler','rotateHandler']
		},
		'stream':{
			'level':'DEBUG',
			'handlers':['streamHandler']
		},
		'tempFile':{
			'level':'DEBUG',
			'handlers':['fileHandler']
		},
		'rotateFile':{
			'level':'INFO',
			'handlers':['rotateHandler']
		}
	},
	'handlers':{
		'streamHandler':{
			'class':'logging.StreamHandler',
			'level':'DEBUG',
			'formatter':'streamFmt',
			'stream':'ext://sys.stdout'
		},
		'fileHandler':{
			'class':'logging.FileHandler',
			'level':'DEBUG',
			'formatter':'streamFmt',
			'filename':'tempFile.log',
			'mode':'w'
		},
		'rotateHandler':{
			'class':'logging.handlers.RotatingFileHandler',
			'level':'INFO',
			'formatter':'rotateFmt',
			'filename':'rotateFile.log',
			'mode':'a',
			'maxBytes':10485760,
			'backupCount':5
		}
	},
	'formatters':{
		'streamFmt':{
			'format':'[ %(levelname)-8s ] %(asctime)s.%(msecs)d %(module)s %(funcName)s %(message)s',
			'datefmt':'%H:%M:%S'
		},
		'rotateFmt':{
			'format':'[ %(levelname)-8s ] %(asctime)s %(module)s %(funcName)s %(message)s'
		}
	}
}

logging.config.dictConfig(LOG_DICT)
log = logging.getLogger("root")
#log.setLevel(logging.NOTSET)# 默认是 WARNING 级别，并且被其他 Handler 继承

log.debug("Debug Testing ...")
log.info("Info Testing ...")
log.warn("Warn Testing ...")
log.warning("Warinig Testing ...")
log.error("Error Testing ...")
log.fatal("Fatal Testing ...")
log.critical("Critical Testing ...")

logging.shutdown()
