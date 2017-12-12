# Python内置的@property装饰器就是负责把一个方法变成属性调用的 方法 -> 属性
class Student(object):
    @property
    def score(self):
        return self._score

    def score(self, value):
        if isinstance(value, int):
            raise ValueError('score must be int')
        if 0 > value or value > 100:
            raise ValueError('score must be 0 ~ 100')
        self.score = value


s = Student()
s.score = 100
print(s.score)
