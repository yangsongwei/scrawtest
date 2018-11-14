# from urllib.robotparser import RobotFileParser
#
# robotfileparse=RobotFileParser()
#
# robotfileparse.set_url('http://www.jianshu.com/robots.txt')
#
# #print(robotfileparse.read())
# print(robotfileparse.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# print(robotfileparse.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))