class Developer(object):
    name = 'mike'
    age = 10
    __sex = 0

    def __init__(self, name, age, sex):
        self.age = age
        self.name = name
        self._sex = sex

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex


class AndriodDeveloper(Developer):

    id = 1242

    def __int__(self, name, age, sex, id):
        super(AndriodDeveloper, self).__init__(name, age, sex)
        self.id = id

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex
        print(self.__sex)


if __name__ == '__main__':
    # androidDeveloper = AndriodDeveloper('23235', 64, 3535,35235)为什么不行
    androidDeveloper = AndriodDeveloper('23235', 64, 3535)
    print(androidDeveloper.id)
    androidDeveloper.set_sex(535)

class PythonDeveloper(AndriodDeveloper):
    def __init__(self, name, age, sex):
        super(PythonDeveloper,self).__init__(name, age, sex)

if __name__ == '__main__':
    pythonCoder = PythonDeveloper('3535',535,64)
    print(pythonCoder.age)
