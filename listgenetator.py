'''
    func:列表生成

'''
#首先生成uri,类似于小说网站的格式
uri=['/article/'+str(i)+'.html' for i in range(1,10)]

print(uri)