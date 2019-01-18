#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from Motion import swipePage, enterContext, click, waittingFor, getToast, findSpecificText
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver import Remote #for keyevent
import random

class script():
	def __init__(self, driver):
		self.driver = driver
		self.sp = swipePage(driver)
		self.ec = enterContext(driver)
		self.ck = click(driver)
		self.wf = waittingFor(driver)
		self.gt = getToast(driver)
		self.ft = findSpecificText(driver)
		reload(sys)
		sys.setdefaultencoding('utf-8')

	def waittingforloginfinish(self):
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/fl_homeHealthVideoTitle")
		self.ck.clickFromManyThingsByResourceID("com.lavidatec.wacareqaexternal:id/home_tab_icon", 2)
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/lin_content")
	def Question(self):
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_ask")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_ask")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/iv_healthForumPostClose")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/ed_healthForumPostArticleTitle")
		title = "我是標題"
		self.ec.enter(title, "com.lavidatec.wacareqaexternal:id/ed_healthForumPostArticleTitle")
		self.ck.clickByString("請將您的問題描述詳細，專家能更精準的為您解答...")
		questionText = str(random.randint(1,1000))
		self.ec.enterSelectByTextviewText(questionText, "請將您的問題描述詳細，專家能更精準的為您解答...")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/cb_healthForumPostAnonymous")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/cb_healthForumPostAnonymous")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/cb_healthForumPostLottery")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/cb_healthForumPostLottery")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_healthForumPostUpload")
		self.gt.search4Toast("上傳完成")
		self.driver.keyevent("4")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
	def QuestionAnonymous(self):
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_ask")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_ask")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/iv_healthForumPostClose")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/ed_healthForumPostArticleTitle")
		title = "我是標題(匿名上傳測試)"
		self.ec.enter(title, "com.lavidatec.wacareqaexternal:id/ed_healthForumPostArticleTitle")
		self.ck.clickByString("請將您的問題描述詳細，專家能更精準的為您解答...")
		questionText = str(random.randint(1,1000))
		self.ec.enterSelectByTextviewText(questionText, "請將您的問題描述詳細，專家能更精準的為您解答...")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/cb_healthForumPostAnonymous")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_healthForumPostUpload")
		self.gt.search4Toast("上傳完成")
		self.driver.keyevent("4")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
	def QuestionNonAnonymous(self):
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_ask")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_ask")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/iv_healthForumPostClose")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/ed_healthForumPostArticleTitle")
		title = "我是標題(非匿名上傳測試)"
		self.ec.enter(title, "com.lavidatec.wacareqaexternal:id/ed_healthForumPostArticleTitle")
		self.ck.clickByString("請將您的問題描述詳細，專家能更精準的為您解答...")
		questionText = str(random.randint(1,1000))
		self.ec.enterSelectByTextviewText(questionText, "請將您的問題描述詳細，專家能更精準的為您解答...")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_healthForumPostUpload")
		self.gt.search4Toast("上傳完成")
		self.driver.keyevent("4")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
	def EditQuestion(self):
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
		self.ck.clickByString("test999")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/iv_forumQuestionDot")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/iv_forumQuestionDot")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/connect_device")
		self.ck.clickByString("編輯")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_healthForumPostUpload")
		target = self.driver.find_element_by_id("com.lavidatec.wacareqaexternal:id/ed_healthForumPostEditor")
		T = target.find_element_by_class_name("android.widget.EditText")
		for i in range(len(T.text)):
			self.driver.keyevent("67")
		T.send_keys("編輯過後的文字!")
		self.ck.clickByString("上傳")
		self.gt.search4Toast("上傳完成")
		#下面利用子元素選擇的方法選擇imagebutton
		self.driver.keyevent("4")
		returnBtn = self.driver.find_element_by_id("com.lavidatec.wacareqaexternal:id/toolbar")
		RBtn = returnBtn.find_element_by_class_name("android.widget.ImageButton")
		RBtn.click()
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
	def DeleteQuestion(self):
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
		self.ck.clickByString("test999")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/iv_forumQuestionDot")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/iv_forumQuestionDot")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/connect_device")
		self.ck.clickByString("刪除")
		self.driver.keyevent("4")
		self.driver.keyevent("4")
	def ReplaySelfQuestioN(self):
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
		self.ck.clickByString("test999")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/iv_forumQuestionDot")
		self.ck.clickByString("回應...")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/cb_forumQuestionAnn")
		replyNum = random.randint(1,1000)
		self.ec.enterSelectByTextviewText(str(replyNum), "回應...")
		self.ck.clickByString("匿名")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/iv_forumQuestionSend")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumQuestionItemDot")
		"""target = self.driver.find_element_by_id("com.lavidatec.wacareqaexternal:id/rv_forumQuestion")
		taarget.find_elements_by_class_name("android.widget.LinearLayout")
		child = target[1]
		replymessage = child.find_element_by_id("com.lavidatec.wacareqaexternal:id/ed_forumQuestionItemEditor")
		checkmessage = replymessage.find_element_by_class_name("android.widget.TextView").text"""
		chekReplayMessage = self.ft.findText(str(replyNum))
		print(chekReplayMessage.text)
	def DeleteReplayMessage(self):
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumTopicTitle")
		self.ck.clickByString("test999")
		self.wf.explicitWaitByResourceID("com.lavidatec.wacareqaexternal:id/iv_forumQuestionDot")
		self.ck.clickByResourceID("com.lavidatec.wacareqaexternal:id/tv_forumQuestionItemDot")
		self.ck.clickByString("刪除")
		self.ft.findText("此留言已被移除")















		





