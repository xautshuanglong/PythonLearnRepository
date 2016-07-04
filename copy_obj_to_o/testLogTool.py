# -*- coding: UTF-8 -*-
from LogTool import LogTool

import sys,os,re,time,shutil

log = LogTool.getLogger()

def ListDir(startDir):
    dirList = os.listdir(startDir)
    for item in dirList:
        log.info("name:{0} isDir:{1}".format(item,os.path.isdir(item)))

def WalkDir(startDir):
    targetList = os.walk(startDir)
    for rootDir,dirs,files in targetList:
#        for dir in dirs:
#	    log.debug("{0} -> {1}".format(rootDir, dir))
#        log.debug(files);
        for file in files:
	    match = re.match(r"(.*)\.obj$", file, re.I)
	    if match:
#                print "abspath ==> ", os.path.abspath(rootDir+'\\'+file)
#                print match.string,'-->' , match.group(0)
		newFileName = file[0:-4]+".o";
#		log.debug("rootDir --> {0}".format(rootDir))
		if os.path.exists(rootDir+'\\'+newFileName) == False:
	            log.info("create new file:{0}".format(rootDir+'\\'+newFileName))
		    CopyToDir(rootDir,file,newFileName)
		else:
		    oldTime = os.path.getmtime(os.path.abspath(rootDir+'\\'+file))
		    newTime = os.path.getmtime(os.path.abspath(rootDir+'\\'+newFileName))
#                    timeStru = time.localtime(lastTime)
                    if newTime < oldTime:
	                log.info("recreate file:{0}".format(rootDir+'\\'+newFileName))
			CopyToDir(rootDir,file,newFileName)
		    else:
		        log.info("Pass file:{0}".format(rootDir+'\\'+file))

def CopyToDir(dirPath,oldName,newName):
    print "inside CopyToDir..."
    if os.path.exists(dirPath+'\\'+oldName):
        print "inside exists branch..."
        shutil.copyfile(dirPath+'\\'+oldName, dirPath+'\\'+newName)
    else:
        log.debug("Do not exists file:{0}".format(dirPath+'\\'+oldName))
		
#       print "last modify time:%d-%d-%d  %d:%d:%d" % (timeStru[0],timeStru[1],timeStru[2],timeStru[3],timeStru[4],timeStru[5])

#    mtime = os.path.getmtime("F:\PythonWorks\copy_obj_to_o\logs\dir1\dir2\obj.txt")

# for testing
if __name__ == "__main__":
#    ListDir("./")
    if len(sys.argv) < 2:
        print "Please input copy path!"
    elif os.path.exists(sys.argv[1]):
        WalkDir(sys.argv[1])
    else:
        print "Bad path,not exist..."
