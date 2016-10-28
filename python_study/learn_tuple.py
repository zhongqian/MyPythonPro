# coding=utf-8
'''
Created on 2016-6-27
 
@author: Administrator
'''

#元组与列表类似，不同之处在于元组的元素不能修改。
print "元组定义："
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6)
tup3 = 'a', 'b', 'c', 'd'
tup4 = ()  #创建一个空元组
tup5 = (50,)  #创建一个只包含一个元素的元组
print tup1
print tup2
print tup3
print tup4
print tup5


#访问元组
print "访问元组："
print tup1[1]
print tup2[1:5]

#修改元组
print "修改元组："
new_tup = tup1 + tup2
print new_tup
#  tup3[2] = "修改的值"  tuple的值不能修改

#删除元组
print "删除元组："
print "tup5:", tup5
del tup5
# print tup5

#元组的运算符：

print "元组的运算符："
print len(new_tup)     #计算元组的个数
print (1, 2, 3) + (4, 5, 6)  #元组连接
print ('Hi!') * 4        #元组复制
print 3 in (1, 2, 3)    #元素是否存在
for x in (1, 2, 3) : print x   #迭代

#元组的内置函数

print "元组的内置函数："
print "cmp()比较两个元组：", cmp((1, 2, 3), (2, 3, 4))
print "len()计算元组的元素个数：", len(tup2)
print "min()返回元组内最小值：", min(tup2)
print "max()返回元组内最大值：", max(tup2)
print "tuple()将一个序列转为元组类型：", tuple([1, 2, 3, 4])


