'''
Created on 2016年10月17日

@author: Administrator
'''
import time
import basecase
from appium import webdriver

def QQLogin(driver, uin = "822991862", psw = "zq4535"):
    time.sleep(3)
    driver.find_element_by_name('登 录').click()
    #进入到登录页面，输入QQ号和密码
    textfields = driver.find_elements_by_class_name('android.widget.EditText')
    textfields[0].set_text(uin)
    #密码是用send_key方法失败，不知道为什么，只能使用set_text()方法
#        textfields[1].send_keys(self.psw)
    textfields[1].set_text(psw)
    driver.find_element_by_name('登 录').click()




if __name__ == '__main__':
    pass