# coding:utf-8
'''
Created on 2016年7月7日

@author: Administrator
'''
def addlist(alist):
    for i in alist:
        yield i + 1
# yield 为一个函数的返回值塞数据

alist = [1, 2, 3, 4]
for x in addlist(alist):
    print x

def h():
    print 'To be brave'
    yield 5
    print 'Fighting'
c = h()
c.next()
# c.next()调用后，h()开始执行，直到遇到yield 5
# c.next()
# 当我们再次调用c.next()时，会继续执行，直到找到下一个yield表达式。由于后面没有yield了，因此会拋出异常

# send(msg)与next()
# 了解了next()如何让包含yield的函数执行后，我们再来看另外一个非常重要的函数send(msg)。其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，只能传递None进去。因此，我们可以看做
# c.next() 和 c.send(None) 作用是一样的。
def h():
    print 'Wen Chuan',
    m = yield 5  # Fighting!
    print m
    d = yield 12
    print 'We are together!'
c = h()
c.next()  # 相当于c.send(None)
c.send('Fighting!')  # (yield 5)表达式被赋予了'Fighting

# 5. send(msg) 与 next()的返回值
# send(msg) 和 next()是有返回值的，它们的返回值很特殊，返回的是下一个yield表达式的参数。比如yield 5，则返回 5 。到这里，是不是明白了一些什么东西？本文第一个例子中，通过for i in alist 遍历 Generator，其实是每次都调用了alist.Next()，而每次alist.Next()的返回值正是yield的参数，即我们开始认为被压进去的东东。我们再延续上面的例子：
def h():
    print 'Wen Chuan',
    m = yield 5  # Fighting!
    print m
    d = yield 12
    print 'We are together!'
c = h()
m = c.next()  # m 获取了yield 5 的参数值 5
d = c.send('Fighting!')  # d 获取了yield 12 的参数值12
print 'We will never forget the date', m, '.', d
