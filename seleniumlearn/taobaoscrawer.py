'''
    func:爬取淘宝商品
    author:monty
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

browser=webdriver.Chrome()
browser.get('https://s.taobao.com/search?initiative_id=staobaoz_20181122&q=ipad')
# search=browser.find_element_by_id('q')
# search.send_keys('ipad')
#
# search.send_keys(Keys.ENTER)

time.sleep(10)

browser.close()

