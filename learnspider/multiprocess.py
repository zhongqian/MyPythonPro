#coding:utf-8
'''
Created on 2016年10月18日  下午7:02:14
@author: Administrator
'''
import requests
from multiprocessing.dummy import Pool as ThreadPool
import time
 
 
def getsource(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HEXCNFN5801708221S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.91 Mobile Safari/537.36 V1_AND_SQ_6.5.5_410_YYB_D QQ/6.5.5.2880 NetType/WIFI WebP/0.4.1 Pixel/1080'}
    html = requests.get(url, headers = headers)
 
if __name__ == '__main__':
    urls = []
    for i in range(1,50):
        newpage = 'http://www.qq.com'
        urls.append(newpage)
 
  # 单线程计时
    time1 = time.time()
    for i in urls:
        print i
        getsource(i)
    time2 = time.time()
 
    print '单线程耗时 : ' + str(time2 - time1) + ' s'
 
  # 多线程计时
    pool = ThreadPool(4)
    time3 = time.time()
    results = pool.map(getsource, urls)
    pool.close()
    pool.join()
    time4 = time.time()
    print '多线程耗时 : ' + str(time4 - time3) + ' s'