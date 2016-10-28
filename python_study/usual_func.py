# coding:utf-8
import sys, locale
from comtypes.gen._0E59F1D2_1FBE_11D0_8FF2_00A0D10038BC_0_1_0 import STRING

# dir()函数可以查看对像内所有属于及方法
print dir([])
print dir(sys)

# tpye()函数是对象数据类型查询的方法
print type(10)
print type("hello, world!")
print type(type(10))

# 格式化输出：这里的%s和%d是占位符，分别是为字符串类型和整型来服务的
print "%s is %d old" % ("she", 20)

# help()函数查看帮助时需要注意哪些问题
print help('sys')
print help('str')
a = [1, 2, 3]
print help(a)
print help(a.append)

# input() ，它希望能够读取一个合法的 python 表达式，
# 即你输入字符串的时候必须使用引号将它括起来，
# 否则它会引发一个 SyntaxError 。
# input() 可接受合法的 python 表达式，举例：input( 1 + 3 ) 会返回 int 型的 4 
str1 = input("input接收 输入你的内容：")
print str1

# raw_input() 将所有输入作为字符串看待，返回字符串类型。
str2 = raw_input("raw_input接收您输入的内容：")
print str2

# raw_input输入中文后，打印 不乱码
info = raw_input('中文输入:').strip().decode(sys.stdin.encoding or locale.getpreferredencoding(True))
print info.encode("GB18030")
