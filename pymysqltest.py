import pymysql

conn=pymysql.connect(host='localhost',user='root',password='root',db='spiders')

cursor=conn.cursor()
def createtable():
    sql='''
        create table students(
            id varchar(20) primary key,
            name varchar(30) not null,
            age int not null)
    '''
    cursor.execute(sql)

conn.close()