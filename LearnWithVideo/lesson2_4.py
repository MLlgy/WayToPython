class Developer(object):
    name = 'mike'
    age = 123
    # 私有变量
    __sex = 0

    # 构造方法
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.__sex = sex

    def get_sex(self):
        return self.__sex
    def set_sex(self,sex):
        self.__sex = sex

    if __name__ == '__main__':
        developer = Developer('e3535','sfsf',1)
