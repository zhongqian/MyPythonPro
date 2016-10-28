# coding=utf-8
'''
Created on 2016-6-27
 
@author: Administrator
'''

x = 20

def func1():
    x = 10
    print"func1内部x的值是：" , x
    return x + 1
print func1()  #函数外部打印x的值

def func2():
    global x   #global地沟油全局变量，x为函数外部的值
    print"func2内部x的值是：", x
    return x + 2

print func2()  #函数外部大于x的值

Money =2000

def AddMoney():
    #这是一个全局变量
    global Money
    Money = Money+1
    
print Money
AddMoney()
print Money

total = 0 #这是一个全局变量

def sum(arg1, arg2):
    #返回两个参数的和
    total = arg1 + arg2 #total在这里是局部变量
    print "函数内是局部变量：", total
    return total
#调用sum函数

sum(10,20)
print "函数外是全局变量：", total