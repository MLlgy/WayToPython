# 线程池

from multiprocessing import Process, Pool
import os, time, random


def long_time_task(name):
    print('run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    print(time)
    time.sleep(random.random() * 3)
    end = time.time()
    # print('start is %s and end is %s' % (start, end))
    print('task %s run time is %0.2f' % (name, (end - start)))


# 对Pool对象调用join()方法会等待所有子进程执行完毕，
# 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

if __name__ == '__main__':
    print('parent process is %s' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done ..')
    p.close()
    p.join()
    print('all subprocess done.')




import subprocess

print()
