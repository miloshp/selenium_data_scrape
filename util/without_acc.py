import csv
import json
from time import sleep
from selenium.webdriver.support import expected_conditions as ExpctC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from util.chromedriver import driver


def without_account(acc_username):

	json_file = open('output/data_json.txt', 'w')
	
	browser, wait = driver()
	
	for username in acc_username:
		browser.get('https://www.instagram.com/{}/'.format(username))

		try:
			if browser.find_element_by_class_name('-vDIg').find_element_by_tag_name('span').is_displayed():
				bio = browser.find_element_by_class_name('-vDIg').find_element_by_tag_name('span').text
		except:
			bio = 'none'

		# try to get the real name / 2nd usrname if exists
		try:
			if browser.find_element_by_class_name('-vDIg').find_element_by_tag_name('h1').is_displayed():
				realname = browser.find_element_by_class_name('-vDIg').find_element_by_tag_name('h1').text
		except:
			realname = 'none'

	
		# get the number of 
		# posts, followers and followings
		post_num = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/a/span').text
		followers_num = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').get_attribute("title")
		accnt_follows = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text
		

		is_verified = False
		try:
			if browser.find_element(By.XPATH, "//*/span[contains(text(),'Verified')]").is_displayed():
				is_verified = True
		except:
			is_verified = False


		# check if private 
		is_private = False
		try:
			if browser.find_element(By.XPATH,"//*/h2[contains(text(),'This Account is Private')]").is_displayed():
				is_private = True
		except:
			is_private = False

		# for csv
		#data = [acc_username, followerNum, followingNum, bio, postnum]

		data = {}
		data[username] = []
		data[username].append({
			'follwers':followers_num,
			'following':accnt_follows,
			'bio':bio,
			'posts':post_num,
			'verified':is_verified,
			'private':is_private,
			'2ndName':realname
			})


		json_file.write(json.dumps(data, indent=4))
		
	browser.quit()





