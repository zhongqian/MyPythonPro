# coding=utf-8
'''
Created on 2016-6-27
 
@author: Administrator
'''

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中

dic1 = {'Alice': 20, 'Bob': 21, 'Jack': 22}
dic2 = {'Name': 'Zara', 'Age': 18, 'Class': 'first'}
print "Name: ", dic2['Name']
print "Age: ", dic2['Age']

# 修改字典

print "修改字典："
dic2["Age"] = 20  # 更新已有字段
dic2['School'] = "WGY School"  # 新增字段
print "dic2['Age']: ", dic2['Age']
print "dic2['School'}: ", dic2['School']

# 删除字典

print "删除字典："
dic = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
del dic['Name']  # 删除键是'Name'的条目
print dic
dic.clear()  # 清空词典所有条目
print dic
del dic  # 删除词典
# print dic

# 字典的特性：
# 字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dic = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}; 
print "dic['Name']: ", dic['Name'];
print dic

# 2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，如下实例：
# dict = {['Name']: 'Zara', 'Age': 7};
#  print "dict['Name']: ", dict['Name'];

# 字典的内置函数和方法
# cmp()函数
print """字典的cmp()函数，比较两个字典，两个字典的元素相同返回0，
如果字典dict1大于字典dict2返回1，如果字典dict1小于字典dict2返回-1"""
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Name': 'Mahnaz', 'Age': 27}
dict3 = {'Name': 'Abid', 'Age': 27}
dict4 = {'Name': 'Zara', 'Age': 7}
print "Return Value : %d" % cmp (dict1, dict2)
print "Return Value : %d" % cmp (dict2, dict3)
print "Return Value : %d" % cmp (dict1, dict4)

# len()函数
print "len()计算字典的长度："
dic = {'Name': 'Zara', 'Age': 7}
print "Length : %d" % len (dic)

# str()函数
print "str()函数，打印字符串输出："
dic = {'Name': 'Zara', 'Age': 7}
print "Equivalent String : %s" % str (dic)

# 字典的方法：
print "字典的方法："
# clear()方法
print "clear()方法清空字典内的所有元素"
dict = {'Name': 'Zara', 'Age': 7};
print "Start Len : %d" % len(dict)
dict.clear()
print "End Len : %d" % len(dict)

# copy()方法
print "copy()方法，返回一个字典的浅复制"
dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = dict1.copy()
print "New Dictinary : %s" % str(dict2)

# fromkeys()方法
print "fromkeys(seq[,value])，以列表seq中的元素做字典的key，value为字典所以key对于的初始值"
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print "New Dictionary : %s" % str(dict)
dict = dict.fromkeys(seq, 10)
print "New Dictionary : %s" % str(dict)

# get()方法
print "get()方法，返回指定key的值，如果不存在返回默认值（None）"
dict = {'Name': 'Zara', 'Age': 27}
print "Value : %s" % dict.get('Age')
print "Value : %s" % dict.get('Sex', "Never")

# has_key()方法
print "has_key()方法，如果key在字典中，返回true，否知返回false"
print "Value : %s" % dict.has_key('Age')
print "Value : %s" % dict.has_key('Sex')

# items()方法：以列表返回可遍历的key，value元组数组
print "items()方法以列表返回可遍历的key，value元组数组"
print "Value : %s" % dict.items()

# keys()方法：以列表返回字典的所有key
print "keys()，已列表返回字典的所有key"
print "keys : %s" % dict.keys()

# values()方法：列表返回字典中的所有值
print "values()方法：列表返回字典中的所有值"
print "Values : %s " % dict.values()

# setdefault()，对指定键不存在于字典中，将会添加键并将值设为默认值，已存在的key不做改变
print "Value : %s" % dict.setdefault('Age', None)
print "Value : %s" % dict.setdefault('Sex', None)
print dict.items()
for item in dict.iteritems():
    print item

# update(dict2)方法把dict2更新到dict中
dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }

dict.update(dict2)
print "Value : %s" % dict

