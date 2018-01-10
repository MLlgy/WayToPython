import os

print('process (%s) start...' % os.getegid())

# 多进程
#
# Unix / Linux操作系统提供了一个fork()
# 系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()
# 调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

pid = os.fork()

if pid == 0:
    print('i am child process (%s) and my parent is (%s).' % (os.getpid(), os.getppid()))
else:
    print('i (%s) create a child process (%s)' % (os.getpid(), pid))
