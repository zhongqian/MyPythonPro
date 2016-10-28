# coding:utf-8
'''
Created on 2016年7月11日  下午4:56:28
@author: Administrator
'''
import os
ls = os.linesep

# 写入相应文件的值
def makeTextFile():
    # get filename
    
    while  True:
        fname = raw_input('Enter you want to write file name: \n')
        if os.path.exists(fname):
            print "ERROR: '%s'already exitsts" % fname
        else:
            break
    
    # get file content (text) lines
    all = []
    print "\nEnter lines ('.' by itself to quit). \n"
    
    # loop until user terminates input
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)
    
    # write lines to file with proper line-ending
    
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print 'DONE'
    
# 读取相应文件的值
def readTextFile():
    # get filename
    fname = raw_input('Enter you want to read filename: ')
    
    # attempt to open file for reading
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error: ", e
    else:
        # display content to the Screen
        for eachLine in fobj:
            print eachLine,
    fobj.close()
    
if __name__ == '__main__':
#     makeTextFile()
    readTextFile()
