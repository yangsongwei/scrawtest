'''
    func:实现简单验证码获取
'''
import pytesseract
from PIL import Image

#首先通过Image打开一个图片
image=Image.open('c1.png')
# #然后通过方法将image对象转化为字符串
# code=pytesseract.image_to_string(image)
# print(code)

#出现错误，需要将图片进行灰度转化和二值处理
image=image.convert('L')
# image2=image1.convert('1')
# image1.show()
threshold = 200
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')
image.show()
code=pytesseract.image_to_string(image)
print(code)

