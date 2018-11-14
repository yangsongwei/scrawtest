from urllib import error,request

try:
    response=request.urlopen('http://cuiqingcai.com/index.htm')
    print(response.read())
except error.URLError as e:
    print(e.reason)
