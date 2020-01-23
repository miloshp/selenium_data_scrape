import requests
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ExpctC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options



def driver():
	options = Options()
	options.add_experimental_option("excludeSwitches", ['enable-automation'])
	options.add_experimental_option('useAutomationExtension', False)

	browser1 = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
	browser1.get('https://www.google.com')
	executor_url = browser1.command_executor._url
	session_id = browser1.session_id

	browser = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
	browser.session_id = session_id
	wait = WebDriverWait(browser,10)

	r = requests.get('https://www.google.com')
	print(r.status_code)

	return browser, wait;
