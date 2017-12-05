import lesson2_5

class JavaCoder(object):
    java_id = 1

    def __init__(self, java_id):
        self.java_id = java_id
        print('javacoder')


class FullStackCoder(JavaCoder,lesson2_5.AndroidDeveloper):

    def __init__(self):
