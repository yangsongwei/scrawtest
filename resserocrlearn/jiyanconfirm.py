'''
    func:斗鱼找回密码,点触式二维码
    author:monty
    date:2018/11/24
'''
from chaojiying import Chaojiying_Client
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from PIL import Image
from io import BytesIO
from selenium.webdriver import ActionChains


tel=18292845394
kind=9004
class CrackGeetest():
    def __init__(self):
        self.url='https://www.douyu.com/member/findpassword/findByPhone'
        self.browser=webdriver.Chrome()
        self.browser.get(self.url)
        self.wait=WebDriverWait(self.browser,20)
        self.tel=tel
        self.chaojiying=Chaojiying_Client('monty123', '19970817',kind)

    def set_tel(self):
        '''
        填写telephonenumber
        :return:
        '''
        #获取输入框
        input=self.wait.until(EC.presence_of_element_located((By.ID,'reg_userphone')))
        input.clear()
        input.send_keys(self.tel)
    def get_geetest_button(self):
        '''
            获取初始验证按钮
        :return:
        '''
        button=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

    # def get_position(self):
    #     """
    #     获取验证码位置
    #     :return: 验证码位置元组
    #     """
    #     img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
    #     time.sleep(2)
    #     location = img.location
    #     size = img.size
    #     top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
    #         'width']
    #     return (top, bottom, left, right)

    def get_image(self):
        '''
            获取验证码图片
        :return: 图片对象
        '''
        image=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_widget')))
        return image

    def get_position(self):
        image=self.get_image()
        time.sleep(2)
        location=image.location
        size=image.size
        top,bottom,left,right=location['y'],location['y']+size['height']-55,location['x'],location['x']+size['width']
        return (top,bottom,left,right)

    def get_screenshot(self):
        '''
        获取整个屏幕截屏
        :return:
        '''
        screenshot=self.browser.get_screenshot_as_png()
        screenshot=Image.open(BytesIO(screenshot))
        return screenshot

    def get_touclick_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha
    def __del__(self):
        self.browser.close()

    def getPoint(self,result):
        '''
        获取每个坐标点
        :param result:
        :return: 返回坐标位置
        '''
        groups=result.get('pic_str').split('|')
        locations=[[int(number) for number in group.split(',')] for group in groups]
        return locations

    def touch_click_words(self,locations):
        '''
        点击坐标
        :param locations:
        :return:
        '''

        for location in locations:
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(self.get_image(), location[0],
                                                                   location[1]).click().perform()
            time.sleep(1)

    def submit(self):
        submit=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_commit')))
        submit.click()
        time.sleep(5)
        button=self.wait.until(EC.element_to_be_clickable((By.ID,'submit-fp-ph')))
        button.click()




if __name__=='__main__':
    cg=CrackGeetest()
    #添加
    cg.set_tel()
    button=cg.get_geetest_button()
    #点击机器验证按钮
    button.click()
    # image=cg.get_position()
    # print(image)
    # time.sleep(10)
    # cg.browser.close()
    #获取验证码截图
    image=cg.get_touclick_image()
    bytes_array=BytesIO()
    image.save(bytes_array,format='PNG')
    #识别验证码
    result=cg.chaojiying.PostPic(bytes_array.getvalue(),kind)
    print(result)
    #获取点击的位置
    locations=cg.getPoint(result)
    cg.touch_click_words(locations)
    cg.submit()