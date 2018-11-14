from urllib import parse

url='http://www.baidu.com/index.html;user?id=5#comment'

#print(parse.urlparse(url).scheme)

# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6&b=10', 'comment']
# print(parse.urlunparse(data))

baseurl='www.baidu.com?'
para={
    'name':'yang',
    'pass':'song'
}

url=baseurl+parse.urlencode(para)

pa=parse.parse_qs(parse.urlparse(url)[4])
print(pa['name'])