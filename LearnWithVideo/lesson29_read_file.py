def read_file():
    try:
        f = open('./file/fileone', 'r')
        print(f.readlines())
    except BaseException as e:
        print(e)
    finally:
        if f:
            f.close()


read_file()


#
def read_byte_file():
    try:
        f = open('./file/235.png', 'r', encoding='gbk', errors='ignore')
        print(f.read())
    except BaseException as e:
        print(e)
    finally:
        if f:
            f.close()


read_byte_file()
