class Student(object):
    pass


s = Student()
s.name = 'mk'
s.age = 12
print('%s, %d' % (s.name, s.age))


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(30)
print(s.age)

# 对一个实例添加的方法对另一个实例不起作用
s2 = Student()

try:
    print(s2.age)
except Exception as err:
    print('os error is {0}'.format(err))
    # raise


# 为类的 所有 实例添加方法
def set_score(self, score, sex):
    self.score = score
    self.sex = sex


Student.set_score = set_score
s.set_score(11, 2)
print('score is %d , sex is %d' % (s.score, s.sex))


# 限制为类添加的属性 用__slots__来限制
class People(object):
    __slots__ = ('age', 'name')


t = People()
try:
    t.sex = 1
    print(t.sex)
except Exception as err:
    print(' error is {0}'.format(err))


class Theacher(People):
    __slots__ = ('sex')


t2 = Theacher()
t2.sex = 2890
print(t2.sex)
