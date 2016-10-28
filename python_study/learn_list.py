# coding=utf-8
'''
Created on 2016-6-27
 
@author: Administrator
'''
from time import time
from __main__ import time

#列表是Python中最基本的数据结构，以进行的操作包括索引，切片，加，乘，检查成员。
list1 = ['physics' , 'chemistry', 2000, 3, 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7];
list3 = ["a", "b", "c", "d"];

#访问列表中的的值
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

#更新列表
print "Value available at index 2 : "
print list1[2]
list1[2] = 2001
print "New value available at index 2 : "
print list1[2]

#删除列表
print list1
del list1[2]
print 'After deleting value at index 2: '
print list1

#列表脚本操作符： + 和 *，+ 号用于组合列表，* 号用于重复列表
print len(list3)
print [1, 2, 3] + [4, 5, 6]
print ['Hi!'] * 4
print 3 in [1, 2, 3]
for x in [1, 2, 3]: print x

#列表的函数和方法
#函数：
print cmp([3, 2], [3, 4])  #比较两个列表的元素
print len(list2)     #列表的个数
print max(list2)     #返回列表元素的最大值
print min(list2)     #返回列表元素的最小值
print list((1, 2, 3))#奖元组转为列表

#方法：
print list1.append('python')   #在列表末尾添加新的对象
print list1.count('python')    #统计某个元素在列表中出现的次数
print list1.extend(list2)      #列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print list1
print list1.index("python")    #从列表中找出某个值第一个匹配项的索引位置
print list1.insert(3, 'learn')  #将对象插入列表
print list1
print list1.pop()              #移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print list1
print list1.remove(3)   #移除列表中的某个值的第一个匹配项
print list1
print list1.reverse()   #翻转列表中元素
print list1
print list1.sort()      #对列表进行排序
print list1


#列表和字典

#Python 字典中使用了 hash table，因此查找操作的复杂度为 O(1)，而 list 实际是个数组，在 list 中，
#查找需要遍历整个 list，其复杂度为 O(n)，因此对成员的查找访问等操作字典要比 list 更快。
t = time()
list = ['a','b','is','python','jason','hello','hill','with','phone','test',
'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd']
# list = dict.fromkeys(list,True)
print list
filter = []
for i in range (1000000):
    for find in ['is','hat','new','list','old','.']:
        if find not in list:
            filter.append(find)
print "total run time:"
print time()-t 