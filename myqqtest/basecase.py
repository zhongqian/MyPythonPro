# coding:utf-8
'''
Created on 2016年10月14日  上午10:14:46
@author: Administrator
'''

import os
from appium import webdriver
import time

def GetDeviceName():
    rt = os.popen('adb devices').readlines()
    zone = rt[1].strip('\t\n')
    return zone

def GetAndroidVersion():
    version = os.popen('adb shell getprop ro.build.version.release').readlines()
    return version

def GetAppPackage():
    PnrPackage = os.popen('adb shell pm list package -f com.tencent.mobileqq').readlines()
    return PnrPackage

def GetAppActivity():
    activity = os.popen('adb shell dumpsys activity')
    return activity

def CleanCache_StartApp():
    os.system('adb shell pm clear com.tencent.mobileqq')
    os.system('adb shell am start com.tencent.mobileqq/.activity.SplashActivity')


def ClickByID(id, driver):
    driver.find_element_by_id(id).click()
    

def ClickByName(id, driver):
    driver.find_element_by_name(id).click()

def GetPic(element, savepath, driver):
    driver.get_screenshot_as_file(savepath)
    
if __name__ == '__main__':
    print GetDeviceName()
    print GetAndroidVersion()
