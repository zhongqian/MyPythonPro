# coding:utf-8
"""
Created on 2016��7��7��

@author: Administrator
"""
import os
import unittest
from appium import webdriver
from time import sleep
from decimal import Context

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            './ContactManager.apk'
        )
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = '.ContactManager'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        #         activity = self.driver.current_activity
        #         context = self.driver.current_context
        #         print activity, context
        self.driver.quit()

    def test_add_contacts(self):
        el = self.driver.find_element_by_accessibility_id("Add Contact")
        el.click()

        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("Appium User")
        textfields[2].send_keys("someone@appium.io")

        self.assertEqual('Appium User', textfields[0].text)
        self.assertEqual('someone@appium.io', textfields[2].text)

        self.driver.find_element_by_accessibility_id("Save").click()

        # for some reason "save" breaks things
        alert = self.driver.switch_to_alert()

        # no way to handle alerts in Android
        self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        self.driver.press_keycode(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
