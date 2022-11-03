from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

browser=webdriver.Chrome('chromedriver.exe')
browser.get('https://www.yahoo.com/')
assert 'Yahoo Search' in browser.title

search=browser.find_element(By.NAME,'p')
search.send_keys('Chennai rains'+Keys.RETURN)

sleep(5)
browser.close()