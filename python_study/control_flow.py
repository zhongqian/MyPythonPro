# coding=utf-8
"""
Created on 2016-6-27

@author: Administrator
"""
from _ast import Num

# 判断条件语句

flag = False
name = 'luren'
if name == 'python':  # 判断变量否为'python'
    flag = True  # 条件成立时设置标志为真
    print "welcome  boss"  # 并输出欢迎信息
else:
    print name  # 条件不成立时输出变量名称

num = 5
if num == 3:  # 判断num的值
    print "boss"
elif num == 2:
    print "user"
elif num == 1:
    print "worker"
elif num < 0:  # 值小于零时输出
    print 'error'
else:
    print "roadman"  # 条件均不成立时输出

num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print "hello"

num = 10
if num <= 0 or num > 10:  # 判断值是否在小于0或大于10
    print 'hello'
else:
    print "undefine"

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print "hello"
else:
    print "undefine"

# 同一行的位置上使用if条件判断语句
var = 100
if (var == 100): print "变量var的值为100"

print "-----------while循环------------"

count = 0
while count < 9:
    print "The count is: ", count
    count = count + 1
print "good bye"

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数是跳出输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立(无限循环）
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break
# for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
count = 0
while count < 5:
    print count, " is  less than 5"
    count = count + 1
else:
    print count, " is not less than 5"

print "-----------for循环----------------"

for letter in "Python":
    print "当前的字母： ", letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print "当前的水果是： ", fruit
print "good bye~"

# 索引迭代
for index in range(len(fruits)):
    print "当前的水果是： ", fruits[index]
print "good bye~"

# for.....else语句
# for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print "%d 等与 %d * %d" % (num, i, j)
            break
    else:
        print num, "是一个质数"

print "------------循环嵌套--------------"
# 嵌套循环输出2~100之间的素数：
print "嵌套循环输出2~100之间的素数："

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print i, "是质数"
    i = i + 1
print "good bye"

# break和continue语句
print "break和continue语句"
# break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print 'Current Letter :', letter

var = 10  # Second Example
while var > 0:
    print 'Current variable value :', var
    var = var - 1
    if var == 5:
        break
print "Good bye!"

# continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print '当前字母 :', letter

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print '当前变量值 :', var
print "Good bye!"
