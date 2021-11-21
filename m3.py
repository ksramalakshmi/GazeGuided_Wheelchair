import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chrome = webdriver.Chrome()
chrome.get('http://127.0.0.1:5500/music/m3.html')

import time
time.sleep(14)
chrome.close() 
