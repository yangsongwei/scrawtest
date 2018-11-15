'''
    func:爬取知乎每日最热话题
    date:2018/11/15
    author:monty
'''
from bs4 import BeautifulSoup as bs
import requests
import lxml
from pyquery import PyQuery as pq

def getPage(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }

    response=requests.get(url,headers=headers)
    return response.text

def pageparse(html):
    soup=bs(html,'lxml')
    result=soup.select('.explore-feed')
    rs=[]
    for i in result:
        r={}
        r['title']=i.find('h2').text.strip()
        r['click']=i.select('.zm-item-vote')[0].text.strip()
        r['author']=i.select('.author-link-line')[0].text.strip()
        r['authorurl']="https://www.zhihu.com"+i.select('span a')[0].attrs['href']
        doc=pq(i.select('.content')[0].text)
        doc.remove('a')
        r['content']=doc.text().strip()
        rs.append(r)
    return rs
def save(items,filename):
    file=open(filename,'a',encoding='utf-8')
    for item in items:
        file.write(item['title']+"\n作者："+item['author']+"\t"*2+"作者联系方式:"+item['authorurl']+"\t"*2+"点赞数："+item['click']+"\n"+item['content'])
        file.write("\n"+"="*120+"\n\n\n")
    file.close()
if __name__=="__main__":
    url='https://www.zhihu.com/explore'
    html=getPage(url)
    rs=pageparse(html)
    save(rs,'zhihu.txt')