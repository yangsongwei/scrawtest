'''
    func:执行cs代码
'''

from selenium import webdriver

browser=webdriver.Chrome()
#
# driver.get('https://www.zhihu.com/explore')
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# driver.execute_script('alert("To Bottom")')
# driver.close()
url = 'https://www.zhihu.com/explore'
browser.get(url)

#选中想要的节点
# node=browser.find_element_by_id('zh-top-link-logo')
# print(node,node.get_attribute('class'))
#获取文本值
n1=browser.find_element_by_class_name('zu-top-add-question')
print(n1.text)

browser.close()
