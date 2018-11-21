from redis import StrictRedis


redis=StrictRedis(host='localhost',port=6379,db=0)
redis.set('name','bog')
redis.set('age',20)
print(redis.get('name'))

