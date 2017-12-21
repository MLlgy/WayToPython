# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Stu(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an int')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 _ 100')
        self._score = value

str = Stu()
str.score = 90
print(str.score)
