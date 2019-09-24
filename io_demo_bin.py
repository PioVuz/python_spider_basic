#coding=utf-8
#Version=python3.6.0
#Tools:Pycharm 2017.3.2
__date__ = '2019/9/24 9:11'
__author__ = 'toaakira'

try:
    import cPickle as pickle
except ImportError:
    import pickle
import os
from multiprocessing import Process
import multiprocessing
# 序列化和反序列化
def test_pickle_dumps():
    d = dict(url='index.html', title='首页', content='首页')
    # dumps = pickle.dumps(d)
    with open(r'G:/test/xx.txt', 'wb') as f:
        pickle.dump(d, f)
    f.close()
def test_pickle_loads():
    with open(r'G:/test/xx.txt', 'rb') as f:
        d = pickle.load(f)
    f.close()
    print(d)

# 使用os模块中的fork方式实现多进程(仅限于linux和unix,mac)
def test_fork():
    print 'current Process (%s) start ...' % (os.getpid())
    pid = os.fork()
    if pid < 0:
        print('error in fork')
    elif pid == 0:
        print('I am child process (%s) and my parent process is (%s)', (os.getpid()), os.getppid())
    else:
        print('I (%s) created a child process (%s).', (os.getpid(), pid))

# 使用multiprocesing模块创建多进程
def run_proc(name):
    print('Child process %s (%s) Running...' % (name, os.getpid()))
def multiprocss_main():
    print('Parent process is %s' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print('Process will start.')
        p.start()
        p.join()
    print('Process End.')


if __name__ == '__main__':
    # test_pickle_loads()
    # test_fork()
    # multiprocss_main
    queue = multiprocessing.Queue()
    pipe = multiprocessing.Pipe()
    
