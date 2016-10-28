#coding:utf-8
'''
Created on 2016-6-27
 
@author: Administrator
'''
import time


class Test:
    """this is a doc string"""
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print "Hello ,",self.name
    

def func():
    """方法的文档注释"""
    print 'fun()'
    print 'time:',time.time()
    

class Stack(object):
    "A well-known data structure..."
    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        x = self.items[-1]
        del self.items[-1]
        return x
    
    def empty(self):
        return len(self.items) == 0

#python中实例对象为啥能按照key赋值（因为类实现了__setitem__和__getitem__方法）
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "point(%s,%s)" % (self.x, self.y)
    
    #实现__getitem__方法
    def __getitem__(self, item):
        return self.__dict__[item]
    
    #实现__setitem__方法
    def __setitem__(self, item, value):
        self.__dict__[item] = value
        

if __name__ == '__main__':
    test=Test('钟迁')
    test.print_name()
    print Test.__doc__  #获取当前的文档注释
    print func.__doc__ 
    func()
    print '#'*20
    x = Stack()
    print x.empty()
    x.push(1)
    print x.empty()
    print x.items
    x.push("hello")
    print x.items
    print x.pop()
    print x.items
    print '#'*20
    p = Point(1, 1)
    print p
    p['x'] = 2
    print p
    p['y'] = 5
    print p
    
