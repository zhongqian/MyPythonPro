# coding=utf8
import time
import calendar

localtime = time.localtime(time.time())
print time.time()
print "本地时间：",localtime

# 获取格式化的时间

f_localtime = time.asctime(localtime)
print "格式化后的本地时间：", f_localtime

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


# 获取某月日历
cal = calendar.month(2016, 5)
print "以下是2016年5月的日历："
print cal

print time.localtime()
print time.time()
