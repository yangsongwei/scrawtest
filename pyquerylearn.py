'''
    func:pyquery库学习
    date:2018/11/15
    author:monty
'''
from pyquery import PyQuery as pq
import requests


def test():
    html = '''
        <div>
            <ul>
                 <li class="item-0">first item</li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
                 <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a></li>
             </ul>
         </div>
        '''
    doc=pq(html)
    #print(doc('li .item-0'))
    for i in doc('.item-1 a').items():
        print(i.attr('href'))


if __name__=="__main__":
    test()

