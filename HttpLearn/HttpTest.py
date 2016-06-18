# encoding:utf-8

from LogTool.LogTool import LogTool
import httplib

log = LogTool.getLogger()

httpConn = None
try:
    httpConn = httplib.HTTPConnection("www.sina.com.cn")
    log.debug("entry try block...")
    httpConn.request('get','/')
    log.debug("after request...")
    response = httpConn.getresponse()
    log.debug("after getresponse")
    print response.status
    print response.reason
    print response.getheaders()
    log.debug("end of try block...")
except Exception,err:
    print err
except:
    print "unknow error occurred"
finally:
    if httpConn:
        httpConn.close()
