#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor, getToast
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver import Remote #for keyevent

class script():
	def __init__(self, driver, apkVersionIdName):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)
		self.apkVersionIdName = apkVersionIdName

	def waittingForLoginFinish(self):
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/fl_homeHealthVideoTitle")
		self.ck.clickFromManyThingsByResourceID(self.apkVersionIdName + "/home_tab_icon", 2)
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/lin_content")
	
	def clickCurrentTopic(self):
		print("------開始測試「點擊當週主題」------\n")	
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_ask")
		self.driver.keyevent("4")
		print("------點擊當週主題測試完成-------\n")
		self.wf.implicitWait(time=3)

	def swipeInTopicPage(self):
		print("------開始測試「主題頁面上下滑動」------\n")
		self.sp.swipeUp(n=2)
		self.sp.swipeDown(n=2)
		self.sp.swipeUp(n=2)
		self.sp.swipeDown(n=2)
		self.sp.swipeDown(n=2)
		self.sp.swipeUp(n=2)
		self.sp.swipeDown(n=2)
		self.sp.swipeDown(n=2)
		self.sp.swipeUp(n=2)
		self.sp.swipeUp(n=2)
		print("------主題頁面上下滑動完成------\n")
		self.wf.implicitWait(time=3)

	def backBtn(self):
		print("-------開始測試「BACK鍵」------\n")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.driver.keyevent("4")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		print("-----「BACK鍵」完成------\n")	
		self.wf.implicitWait(time=3)

	def checkArticle(self):
		print("-----開始測試「查看全文」------\n")
		self.ck.clickByResourceID(self.apkVersionIdName + "/tv_forumTopicTitle")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_more")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/iv_themeDetailClose")
		self.ck.clickByResourceID(self.apkVersionIdName + "/iv_themeDetailClose")
		self.wf.explicitWaitByResourceID(self.apkVersionIdName + "/tv_ask")
		print("-----「查看全文」完成-----\n")
		self.wf.implicitWait(time=3)


		
		
		
		



		