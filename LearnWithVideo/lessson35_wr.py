with open('./file/fileone') as f:
    print(f.read())


with open('./file/fileone','w') as f:
    f.write('hello python, i am a boy')


from io import StringIO
f = StringIO
# f.write('hello python')