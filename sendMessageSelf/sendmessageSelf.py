#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 

import os
import unittest
from appium import webdriver
from sendmessageSelfScript import script
from apkVersionAndCellConfig import Config


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WaCareTest(unittest.TestCase):
	def setUp(self):
		configfile = Config()
		self.driver = configfile.getDriver()
		self.driver.implicitly_wait(10)#隱式等待
		self.apkVersionIdName = configfile.getApkVersionIdName()

	def tearDown(self):
		self.driver.quit()

	def test(self):
		test = script(self.driver, self.apkVersionIdName)
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
