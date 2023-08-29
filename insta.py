from selenium import webdriver
from selenium.Webdriver.common.Keys import Keys
import time

driver = webdriver.Chrome('Chromedriver.exe')
driver.get('https://www.instagram.com')

time.sleep(2)
e = driver.find_element_by_css_selecter('input[name="username"]')
e.send_keys('내 아이디')
e.send_keys(Keys.ENTER)



