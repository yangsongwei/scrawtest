'''
    func:generator演示
'''

def getUpper(a):
    for i in a:
        yield i.upper()

if __name__=='__main__':
    for i in getUpper([chr(i) for i in range(97,123)]):
        print(i)