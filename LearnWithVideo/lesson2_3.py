class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_data(self):
        print('name is %s,age is %d' %(self._name,self.age))

stu = Student('mk',25)
print(stu.get_data)
print(stu._name)

def data(*y):
    print(y)
data(142,141)
data('345',3535,898.8)


# 关键字参数,收到的是一个dic
def data1(x,**y):
    print(x,y)
data1(353)
data1('et',tmt='te',age=353)


# 全局变量

gol = 123

def data2():
    global gol
    gol = 3434
    print(gol)
data2()
