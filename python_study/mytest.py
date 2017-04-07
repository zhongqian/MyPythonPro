# coding:utf-8
"""
Created on 2017/4/7  17:50
@author: Administrator
"""


def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList("a")
"""
很多人都会误认为list1=[10],list3=[‘a’],因为他们以为每次extendList被调用时，列表参数的默认值都将被设置为[].但实际上的情况是，新的默认列表只在函数被定义的那一刻创建一次。

当extendList被没有指定特定参数list调用时，这组list的值随后将被使用。这是因为带有默认参数的表达式在函数被定义的时候被计算，不是在调用的时候被计算。因此list1和list3是在同一个默认列表上进行操作（计算）的。而list2是在一个分离的列表上进行操作（计算）的。（通过传递一个自有的空列表作为列表参数的数值）。

extendList的定义可以作如下修改。

尽管，创建一个新的列表，没有特定的列表参数。
下面这段代码可能能够产生想要的结果。
"""


def extendlist(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list


list4 = extendlist(10)
list5 = extendlist(123, [])
list6 = extendlist("a")

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass


if __name__ == "__main__":
    print "list1 = %s" % list1
    print "list2 = %s" % list2
    print "list3 = %s" % list3

    print "list4 = %s" % list4
    print "list5 = %s" % list5
    print "list6 = %s" % list6

    print Parent.x, Child1.x, Child2.x
    Child1.x = 2
    print Parent.x, Child1.x, Child2.x
    Parent.x = 3
    print Parent.x, Child1.x, Child2.x
