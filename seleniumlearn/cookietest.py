'''
    func:cookie操作
'''
from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
#获取cookie信息
print(browser.get_cookies())
#添加cookie信息
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})

print(browser.get_cookies())
#删除所有的cookie
browser.delete_all_cookies()
print(browser.get_cookies())
browser.close()