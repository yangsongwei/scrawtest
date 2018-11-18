'''
    func:pymysql练习
    author：monty
    date:2018/11/15
'''

import pymysql

con=pymysql.connect(host='localhost',user='root',password='root')
cursor=con.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
con.close()
