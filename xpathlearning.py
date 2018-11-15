'''
    func:xpath库练习
    date:2018/11/15
    author:monty
'''
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
#将text文本转为HTML对象
html=etree.HTML(text)
result=etree.tostring(html)

# print(result.decode('utf-8'))
res=html.xpath('//li[position()>1]/a/text()')

print(res)