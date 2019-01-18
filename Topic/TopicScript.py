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
	def __init__(self, driver):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)
	
	def Topic(self):
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/fl_homeHealthVideoTitle")
		self.ck.clickFromManyThingsByResourceID("com.lavidatec.wacareqaexternal:id/home_tab_icon", 2)
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/lin_content")
		print("------開始測試「點擊當週主題」------\n")	
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_ask")
		self.wf.implicitWait()
		print("------點擊當週主題測試完成-------\n")
		self.wf.implicitWait(time=3)
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
		print("-------開始測試「BACK鍵」------\n")
		self.driver.keyevent("4")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
		print("-----「BACK鍵」完成------\n")	
		self.wf.implicitWait(time=3)
		print("-----開始測試「查看全文」------\n")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/iv_more")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/iv_themeDetailClose")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/iv_themeDetailClose")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_ask")
		print("-----「查看全文」完成-----\n")
		self.wf.implicitWait(time=3)



		