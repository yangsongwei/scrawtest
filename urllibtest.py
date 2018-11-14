# -*- charset:utf-8 -*-
'''
    date:2018/11/13
    function:urllibtest
    author:monty
'''
from urllib import parse,request

# response=urllib.request.urlopen('http://www.python.org')
# #print(response.read().decode('utf-8'))
# print(response.status)
# print(response.getheader('Server'))

# request=urllib.request.Request('http://www.baidu.com');
#
# response=urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

url='http://httpbin.org/post'
#设置header信息
headers={
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
    'Host':'httpbin.org'
}

dict={
    'name':'Germey'
}
#传入参数
data=bytes(parse.urlencode(dict),encoding='utf8')
req=request.Request(url=url,data=data,headers=headers,method='POST')
response=request.urlopen(req)

print(response.read().decode('utf-8'))





















