# encoding:utf-8

from LogTool.LogTool import LogTool
import httplib

log = LogTool.getLogger()

httpConn = None
try:
    httpConn = httplib.HTTPConnection("192.168.1.110", 9090)
    httpConn.request('GET','/index.html')
    response = httpConn.getresponse()
    print response.status
    print response.reason
    print response.getheaders()
    log.debug(response.read())
    log.debug("end of try block...")
except Exception,err:
    print "Error:",err
except:
    print "unknow error occurred"
finally:
    if httpConn:
        httpConn.close()
