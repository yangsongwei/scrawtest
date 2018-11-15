'''
    func:爬取猫眼排名前一百的电影详细信息
    date:2018/22/15
    author:monty
'''
import requests
import re
import json
url='http://maoyan.com/board/4'


def getPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Cookie': '__mta=150305033.1542195769568.1542195769568.1542195769568.1; uuid_n_v=v1; uuid=66B6E140E80211E8B75C2DD07DD203F6788C2125FF0241418B0B4B4FD68D12B6; _csrf=f199ca61f941af1aa9120deb108c8404bbbaede93e57359da9d569489c9603b5; _lxsdk_cuid=1671207ebb4c8-05733a798bb5cb-4313362-100200-1671207ebb534; _lxsdk=66B6E140E80211E8B75C2DD07DD203F6788C2125FF0241418B0B4B4FD68D12B6; _lxsdk_s=1671207ebb7-11c-99f-4be%7C%7C2'
    }
    response = requests.get(url, headers=headers)
    pattern = '<p class="name">.*?>(.*?)</a>.*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
    results=re.findall(pattern,response.text,re.S)
    for result in results:
       yield {
           'name':result[0],
           'actor':result[1].strip()[3:],
            'time':result[2].strip()[5:]
       }
    return results
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
for i in range(0,10):
    if i==0:
        items=getPage(url)
    else :
        items=getPage(url+'?offset='+str(10*i))
    for item in items:
        write_to_file(item)