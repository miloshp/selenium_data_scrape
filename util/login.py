import csv
from time import sleep
from selenium.webdriver.support import expected_conditions as ExpctC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from util.chromedriver import driver



def login_insta(acc_username):
	browser, wait = driver()
	browser.maximize_window()
	# implicit wait 20
	browser.implicitly_wait(20)
	# navigate to specific web page
	browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

	username = "***********"
	password = "***********"

	# enter username 
	usern = wait.until(ExpctC.visibility_of_element_located((By.XPATH, ".//input[@name='username']")))
	usern.send_keys(username)

	# enter password
	passwrd = wait.until(ExpctC.visibility_of_element_located((By.XPATH, ".//input[@name='password']")))
	passwrd.send_keys(password)

	# instead of looking for sumbit button, just press enter when done with password and username 
	submit = browser.find_element_by_tag_name('form')
	submit.submit()

	print('logged in')

	sleep(4)

	# if pop-up shows, click not now 
	popUP = browser.find_element_by_xpath('/html/body/div[4]/div')
	
	if popUP:
		not_now_bttn = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
		not_now_bttn.click()

	# find search bar 
	input_search = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
	input_search.send_keys(acc_username)

	sleep(3)
	# select the first result
	select = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a').click()

	sleep(2)
	followerNum = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text
	print(followerNum)

    # get the number of profile followings
	followingNum = int(browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text)
	print(followingNum)

	# get bio from the profile
	bio = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/span').text
	print(bio)

	# open following tab on profile
	follow = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()

	csv_file = open('output/profile_folowing.csv', 'w')

	#find all li elements in list
	fBody  = browser.find_element_by_xpath("//div[@class='isgrP']")
	followTR = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')

	#browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody) 
	for i in range(1, 13):
		# get the name of the user in following tab 
		getNameOfUser = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[(%d)]/div/div[2]/div[1]/div/div/a' %i).text
		sleep(1)
		print(getNameOfUser)
		#write data to csv
		data = [getNameOfUser]
		writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
		writer.writerow(data)
	
	browser.execute_script('arguments[0].scrollBy(0,300);', fBody)
	sleep(4)

	for i in range(13, int(follownumber)):
		getNameOfUser = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[(%d)]/div/div[1]/div[2]/div[1]/a' %i).text
		sleep(3)
		print(getNameOfUser)
		browser.execute_script('arguments[0].scrollBy(0,100);', fBody)
		data = [getNameOfUser]
		writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
		writer.writerow(data)


	sleep(2)
	
	browser.quit()