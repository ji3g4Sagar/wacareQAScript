#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 

import os
import unittest
from appium import webdriver
from sendmessageSelfScript import script


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WaCareTest(unittest.TestCase):
	def setUp(self):
		desired_caps = {} # Appium收到http Request後會解析這個key-value pair
		app = ('http://35.194.192.102:5000/getfile?filename=qaExternalWaCare-v1.0.3.1.1.apk')
		desired_caps['app'] = app
		desired_caps['platformName'] = 'Android' #定義測試的系統環境
		desired_caps['platformVersion'] = '5.1.1' #定義版本
		desired_caps['deviceName'] = 'Android Emulator' #定義裝置名稱
		desired_caps['automationName'] = 'uiautomator2'
		desired_caps['noReset'] = 'true'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(10)#隱式等待

	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver)
		test.waittingforloginfinish()
		print("------Start Question test------\n")
		test.Question()
		print("-----Question test finish!!!!!!!!!!\n")
		self.driver.implicitly_wait(3)
		print("-----Start QuestionAnonymous test-------\n")
		test.QuestionAnonymous()
		print("-----QuestionAnonymous test finish!!!!!!\n")
		self.driver.implicitly_wait(3)
		print("-----Start QuestionNonAnonymous test-----\n")
		test.QuestionNonAnonymous()
		print("-----QuestionNonAnonymous test finish!!!!!\n")
		self.driver.implicitly_wait(3)
		print("-----Start EditQuestion test-------\n")
		test.EditQuestion()
		print("------EditQuestion test finish!!!!!!\n")
		self.driver.implicitly_wait(3)
		print("-----Start DeleteQuestion test------\n")
		test.DeleteQuestion()
		print("-----DeleteQuestion test finish!!!!!\n")
		self.driver.implicitly_wait(3)
		print("------Start ReplaySelfQuestioN test------\n")
		test.ReplaySelfQuestioN()
		print("ReplaySelfQuestioN test finish!!!!!!\n")
		self.driver.implicitly_wait(3)
		print("-----Start DeleteReplayMessage test-----\n")
		test.DeleteReplayMessage()
		print("-----DeleteReplayMessage test finish!!!!!!\n")
		self.driver.implicitly_wait(3)
		






if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WaCareTest)  
    unittest.TextTestRunner(verbosity=0).run(suite)