import requests
from requests import exceptions

# d={
#     'name':'yang',
#     'pass':'monty'
# }
# try:
#添加header信息
# headers={
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r=requests.get('https://github.com/favicon.ico',headers=headers)
# with open('1.ico','wb') as f:
#     f.write(r.content)
# except exceptions.BaseHTTPError as e:
#     print(e.reason())


#文件上传
# files={'1.ico':open('1.ico','rb')};
#
# response=requests.post('http://httpbin.org/post',files=files)
#
# print(response.text)

#利用cookie信息登录知乎
# headers={
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
#     'Host':'www.zhihu.com',
#     'Cookie':'_zap=03baf899-d238-4993-9e41-d32859850724; d_c0="AEBomaPtfA6PTqydZQ-NYpDwzWdW3yJpLhA=|1541681963"; q_c1=62578b0940b04ff2ae4305ae50bbde9a|1541681966000|1541681966000; l_cap_id="MTEyZmM5ODhmN2E5NDI3ZDhiMmJmNDNhZGNmNmViNzY=|1541682009|fec0dbbc6af5aafa63706fe860ecd57dca72aa70"; r_cap_id="MDM0NjlkODQxMzM4NGEyNzg0ZWMwMGFjODI5MjVlN2Y=|1541682009|0b864dd3c7162ccd34d218904618b7df50047e6d"; cap_id="MjY3MTBlNWQwYjY3NGM5M2JkNGRkYWExNmU0MTRkOGQ=|1541682009|67aeca16235c670c3a192ba8cf35dda7f1d99012"; _xsrf=w50Gcg4781c7y3h2RvtBJnWdAGoVm2PA; capsion_ticket="2|1:0|10:1542181909|14:capsion_ticket|44:YmIxZWFhMDc5MzY1NGVhODhhYWE0N2FmMjFkMjc0MmM=|94b7bd5f597cccedd5f29acf6bd614ab9bc02559315ff946cc4fa0fe0dccec7c"; z_c0="2|1:0|10:1542181949|4:z_c0|92:Mi4xb2F0LUFnQUFBQUFBUUdpWm8tMThEaVlBQUFCZ0FsVk5QU0xaWEFDTklxeFRDaXRqVWtYZFJLQjFlaFgybXFkVEhn|2e3ea7673323aa80c2250f2a4644b63dda6e55e97c0f87b67f370d7918ca291e"; tst=r; tgw_l7_route=e0a07617c1a38385364125951b19eef8; __gads=ID=d0372d161df30251:T=1542183153:S=ALNI_Mb2zT1zfCgWf2-cg95PWzhPLXyj-Q'
# }
#
# respose=requests.post('https://www.zhihu.com',headers=headers)
# print(respose.text)

#维持会话
# request=requests.Session()
# request.post('http://httpbin.org/cookies/set/number/123456789');
#
# reponse=request.post('http://httpbin.org/cookies')
# print(reponse.text)

#验证ssl

# resonse=requests.post('https://www.12306.cn',verify=False)
# print(resonse.text)






















