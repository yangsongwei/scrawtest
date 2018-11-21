'''
    func:类的定义和使用
    author:monty
'''


#定义student类
class Student:
    def __init__(self,id,score,name):
        #定义公有变量
        self.id=id
        #定义私有变量，前面两个__
        self.__score=score
        self.__name=name

    def getInfo(self):
        return {'name':self.__name,'score':self.__score}

class High(Student):
    pass

if __name__=='__main__':
    #切记定义对象时不能使用new
    s1=Student(1,'98','monty')
    s2=Student(2,'59','yang')

    print(s1.getInfo())
    print(s2.getInfo())
    #会报错
    #print(s1.__score)