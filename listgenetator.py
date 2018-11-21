# '''
#     func:列表生成
#
# '''
# #首先生成uri,类似于小说网站的格式
# uri=['/article/'+str(i)+'.html' for i in range(1,10)]
#
# print(uri)
# #一般上面的内容为爬虫爬到的
#
# #下面是需要进行处理的内容
# url=['http://biquge'+i for i in uri]
#
# print(url)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ i.upper() for i in L1 if isinstance(i,str)]
print(L2)