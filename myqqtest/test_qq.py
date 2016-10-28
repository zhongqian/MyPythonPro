#coding:utf-8
'''
Created on 2016年10月14日

@author: Administrator
'''
import unittest
from appium import webdriver
import basecase
import time
import testcase
from testcase import QQLogin

class Test(unittest.TestCase):

    def setUp(self):
        basecase.CleanCache_StartApp()
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.tencent.mobileqq'
        desired_caps['appActivity'] ='.activity.RegisterGuideActivity'
    
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        QQLogin(self.driver)

    def tearDown(self):
        if (self.driver !=None):
            self.driver.quit()

    def testPass(self):
        
        time.sleep(30)
        print 'pass~~'

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()