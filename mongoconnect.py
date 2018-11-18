'''
    func:mongodb连接
    date:2018/11/16
    author:monty
'''

import pymongo

mongo=pymongo.MongoClient(host='localhost')
# print(mongo.server_info())

#指定数据库
db=mongo.test
collection=db.students
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

# result=collection.insert(student)

# print(result)
# result=collection.insert_one(student)
# print(result.inserted_id)

#查询
result=collection.find({'name':'Jordan'})
print(result.count())


















