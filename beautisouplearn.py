'''
    func:beautisoup库学习
    date:2018/11/15
    author:monty
'''

from bs4 import BeautifulSoup as bs
import re
# soup=bs('<p>beasdfM</p>','lxml')
# print(soup.p.string)

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup=bs(html,'lxml')
#print(soup.prettify())
#print(soup.p.attrs['class'])

# print(soup.body.children)
# for i, child in enumerate(soup.body.descendants):
#     print(i,child)

# for i in soup.find_all(text=re.compile('.*?a.*?')):
#     print(i)

print(soup.select('.title')[0].string)