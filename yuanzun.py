'''
    func:爬取元尊最新章节
    date:2018/11/18
    author:monty
'''

import requests
from pyquery import PyQuery as pq

def getPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }

    response=requests.get(url,headers=headers)
    return response.text

def parse(html):
    doc=pq(html)

    items=doc.find('dd a')
    a=[]
    for item in items.items():
        a.append(item.attr('href'))
    return a

#获得每一章内容
def getContent(a):
    content=[]
    for i in a:
        content.append(getPage(i))

    return content

#获取每章的内容
def parseContent(content):
    book=[]
    for i in content:
        neirong={}
        d=pq(i)
        neirong['title']=d('.content h1').text().strip()
        neirong['content']=d('.content .showtxt').remove('a').text().strip()
        book.append(neirong)
    return book

#保存内容
def save(items,filename):
    file=open(filename,'a',encoding='utf-8')
    for item in items:
        file.write(item['title']+"\n"+item['content'])
        file.write("\n"+"="*120+"\n\n\n")
    file.close()

#对文章内容进行处理
def change(content):
    c=content.split('\n')
    print(c)
if __name__=='__main__':
    url='https://www.ddbiquge.cc/'
    html=getPage(url)
    # print(html)
    a=parse(html)
    a=[url[:-1]+i for i in a]
    content=getContent(a)
    book=parseContent(content)
    # for b in book:
    #     change(b['content'])
    # change(book[0]['content'])
    save(book,'story.txt')