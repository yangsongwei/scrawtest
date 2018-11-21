'''
    func:ajax练习
    author:monty
    date:2018/11/20
'''

from urllib.parse import  urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url='https://m.weibo.cn/api/container/getIndex?'
client=MongoClient(host='localhost')
db=client.weibo
collection=db.weibo

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_page(page):
    #设置请求参数
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page
    }
    #将请求参数转化为get请求参数形式
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(json):
    if json:
        items=json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo


#将信息保存到mongo数据库
def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')

if __name__ == '__main__':
    for page in range(1, 15):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)








