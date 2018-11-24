'''
    func:点触式验证码
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time


email='1325380224@qq.com'
password='monty19970817'
softid='897848'
kind=9104

class CrackTouclick():
    def __init__(self):
        self.url=''
        self.browser=webdriver.Chrome()
        self.browser.get(self.url)
        self.wait=WebDriverWait(self.browser,20)
        self.email=email
        self.password=password
        self.softId=softid
        self.kind=kind

    def insert_data(self):
        emailinput=self.wait.until(EC.presence_of_element_located((By.ID,'email')))
        emailinput.send_keys(self.email)
        passwordinput=self.wait.until(EC.presence_of_element_located((By.ID,'password')))
        # time.sleep(10)
        passwordinput.send_keys(self.password)

    def get_button(self):
        '''
        获取按钮
        :return:
        '''
        button=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button


if __name__ == '__main__':
	# chaojiying = Chaojiying_Client('monty123', '19970817', '897848')	#用户中心>>软件ID 生成一个替换 96001
	# im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
	# print(chaojiying.PostPic(im, 1902))

    test=CrackTouclick()
    test.insert_data()
    button=test.get_button()

    button.click()

    time.sleep(20)

    test.browser.close()