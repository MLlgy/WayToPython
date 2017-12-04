class Student(object):
    pass
bar = Student()
print(bar)

bar.name = 'name'
print(bar.name)

class Student2(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printattri(self):
        print('name is %s,age is %d' %(self.name,self.age))

stu = Student2('json',12)
print('name is %s, age is %d' % (stu.name ,stu.age))
print(stu.printattri)