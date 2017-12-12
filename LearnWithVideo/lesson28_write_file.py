def write_file():
    try:
        f = open('/home/mk.io/下载/python视频/WayToPython/LearnWithVideo/fileone','w')
        f.write('hello python')
    except BaseException as e:
        print(e)
    finally:
        if f:
            f.close()


write_file()
