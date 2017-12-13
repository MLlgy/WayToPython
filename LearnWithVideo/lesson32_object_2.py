# 定制类
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'student name is %s' % self.name
    # __repr__ = __str__()


print(Student('name'))


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)


class Fib2(object):

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
            return a


f = Fib2()
print(f[3])


# __getattr__
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
class Teacher(object):

    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'age':
            return 12
        raise AttributeError('\'Teacher\' object has no attribute \'%s\'' % attr)


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)

# __call__
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student2(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('my name is %s', self.name)


s = Student2('ete')
s()
