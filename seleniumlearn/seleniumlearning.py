from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

#完成浏览器对象的初始化并赋值为browser对象
browser=webdriver.Chrome()
# browser=webdriver.Edge()
try:
    #访问百度网址，然后获得源代码
    browser.get('https://www.baidu.com')
    #根据id来获取节点
    input=browser.find_element_by_id('kw')
    input.send_keys('python')
    # input.send_keys(Keys.ENTER)
    button=browser.find_element_by_id('su')
    button.click()
    wait=WebDriverWait(browser,10)
    wait.until(ec.presence_of_all_elements_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    pass

