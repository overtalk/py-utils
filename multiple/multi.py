# coding=utf-8
from time import ctime,sleep
import threading


def music(name):
    for i in range(3):
        print("listen %s - %s" % (name, ctime()))
        sleep(1)


def movie(name):
    for i in range(2):
        print("watching %s - %s" % (name, ctime()))
        sleep(3)



t1 = threading.Thread(target=music, args=(u'爱情买卖',))
t2 = threading.Thread(target=movie, args=(u'阿凡达',))
threads = [t1, t2]

if __name__ == '__main__':
    for t in threads:
        # 声明线程为守护线程，如果不设置为守护线程程序会被无限挂起
        t.setDaemon(True)
        t.start()
    # join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞
    t.join()
    print('all over %s' % ctime())