# coding=utf-8
'''
Created on 2016-6-27
 
@author: Administrator
'''
import os
from python_study.myclass import learn_class

print "#打印learn_class模块中的__doc__属性"
#打印learn_class模块中的__doc__属性
print learn_class.__doc__
print learn_class.Test.__doc__
print learn_class.func().__doc__
print learn_class.__name__

print '---------------------------------'
p = '../appinumtest/ContactManger.apk'

print os.path.join(os.path.dirname(__file__),p)

print os.path.abspath(os.path.join(os.path.dirname(__file__),p))
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
print PATH
print '----------------------------------'

arr = [1, 2, 3, 4]
arr_cp = arr
arr_cp[0] = 100
#print打印出[100, 2, 3, 4]
print arr

a = 100

#你可能想先打印a的值，再对a的值进行修改
def myfunc():
    global a 
    print a
    a = 200
    print a
myfunc()

def saver(x=[]):
    x.append(1)
    print x

saver() # 打印[1]
saver() # 打印[1,1]
saver() # 打印[1,1,1]

#正确的写法
# def saver(x=None):
#     if x is None: x = []
#     x.append(1)
#     print x