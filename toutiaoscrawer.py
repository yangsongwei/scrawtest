'''
    func:爬取头条街拍美图
    author:monty
    date:2018/11/21
'''

from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
import json
import os
from hashlib import md5

base_url='https://www.toutiao.com/search/?'

param={
    'keyword':'街拍'
}

url=base_url+urlencode(param)
# print(url)
headers={
    'Host':'https://www.toutiao.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'referer':url,
    'X-Requested-With':'XMLHttpRequest'
}

def getonePage(offset):
    b_url='https://www.toutiao.com/search_content/?'
    params={
        'offset':str(offset),
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab',
    }

    url=b_url+urlencode(params)
    try:
        reponse=requests.get(url)
        if reponse.status_code==200:
            return reponse.json()
    except requests.ConnectionError as e:
        print('error',e.args)

def parseData(json1):
    if json1:
        data=json1.get('data')
        for item in data:
            data1={}
            if item.get('cell_type'):
                continue
            # data1['abstract']=item.get('abstract')
            data1['article_url']=item.get('article_url')
            data1['title']=item.get('title')
            data1['image_url']=['https:'+i['url'] for i in item.get('image_list')]
            yield data1

#保存图片
def save_image(items):
    for item in items:
        if not os.path.exists('头条/'+item.get('title')):
            os.mkdir('头条/'+item.get('title'))
        for image_url in item.get('image_url'):
            try:
                response = requests.get(image_url)
                if response.status_code == 200:
                    file_path = '{0}/{1}.{2}'.format('头条/'+item.get('title'), md5(response.content).hexdigest(), 'jpg')
                    if not os.path.exists(file_path):
                        with open(file_path, 'wb') as f:
                            f.write(response.content)
                    else:
                        print('Already Downloaded', file_path)
            except requests.ConnectionError:
                print('Failed to Save Image')


if __name__=='__main__':
    for i in range(8):
        json1=getonePage(i*20)
        toutiao=parseData(json1)
        save_image(toutiao)