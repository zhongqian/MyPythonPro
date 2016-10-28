# coding:utf-8
'''
Created on 2016年7月7日

@author: Administrator
'''
from uiautomator import device as d
import time
import os


def login(clear=True, uin='822991868', psw='zq4535'):
    print "1. Clear cache"
    os.system('adb shell pm clear com.tencent.mobileqq')
    print "2. Launching QQ"
    os.system('adb shell am start com.tencent.mobileqq/.activity.SplashActivity')
    time.sleep(8)

    # 输入QQ和密码
    print "3. Input QQ and PSW"
    if d(text='登 录', className='android.widget.Button').exists:
        d(text='登 录', className='android.widget.Button').click()

    d(text='QQ号/手机号/邮箱', className='android.widget.EditText').set_text(uin)
    d(index='2', className='android.widget.EditText').set_text(psw)
    d(text='登 录', className='android.widget.Button').click()
    time.sleep(8)

    # 跳过绑定电话号码页面
    d(index='0', className='android.widget.TextView').click()
    # d.press('back')
    print "4. Login success~"


if __name__ == '__main__':
    login()
