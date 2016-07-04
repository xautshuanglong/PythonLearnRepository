# encoding:utf-8

import os,threading,logging,logging.config

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
			'filename':'./logs/tempFile.log',
			'mode':'w'
		},
		'rotateHandler':{
			'class':'logging.handlers.RotatingFileHandler',
			'level':'INFO',
			'formatter':'rotateFmt',
			'filename':'./logs/rotateFile.log',
			'mode':'a',
			'maxBytes':10485760,
			'backupCount':5
		}
	},
	'formatters':{
		'streamFmt':{
			'format':'[ %(levelname)-5s ] %(asctime)s.%(msecs)d %(module)s %(message)s',
			'datefmt':'%H:%M:%S'
		},
		'rotateFmt':{
			'format':'[ %(levelname)-5s ] %(asctime)s %(module)s %(message)s'
		}
	}
}

def logToolInit():
    checkLogsDir()
    logging.config.dictConfig(LOG_DICT)
    LogTool._log = logging.getLogger("root")

def checkLogsDir():
    logsDir = os.path.abspath(".")+"\\logs"
    if not os.path.exists(logsDir):
        os.mkdir(logsDir)

class LogTool(object):
    
    _instance = None
    _log = None
    _lock = threading.Lock()

    def __init__():
        print "disable the __init__ method"

    @staticmethod
    def getLogger():
        if not LogTool._instance:
            LogTool._lock.acquire()
            if not LogTool._instance:
                LogTool._instance = object.__new__(LogTool)
                object.__init__(LogTool._instance)
                logToolInit()
            LogTool._lock.release()
        return LogTool._instance

    def debug(self,msg=None):
        if msg:
    		LogTool._log.debug(msg)

    def info(self,msg=None):
        if msg:
    		LogTool._log.info(msg)
    
    def warn(self,msg=None):
        if msg:
    		LogTool._log.warn(msg)
    
    def error(self,msg=None):
        if msg:
    		LogTool._log.error(msg)

    def shutdown(self):
        logging.shutdown()
