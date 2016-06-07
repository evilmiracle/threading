#!/usr/bin/python
# -*- coding: UTF-8 -*-


import threading
import time

exitFlag = 0


class myThread(threading.Thread):  # 继承父类

    def __init__(self, threadID, name, counter):  # 　重写init
        threading.Thread.__init__(self)
        self.threadID = threadID  # 线程ID
        self.name = name  # 线程名
        self.counter = counter  # 计数器

    def run(self):  # many thread running 主函数
        print "starting" + self.name  # 输出当时running thread name
        print_time(self.name, self.counter, 5)  # transfer print_time function
        print "Exiting" + self.name  # printf running thread name


def print_time(threadName, delay, counter):  # 每个参数对应 self.name self.conunter 5
    while counter:  # 此时counter = 5
        if exitFlag:
            thread.exit()
        time.sleep(delay)  # 启动thread的 1 和 2
        print "%s:%s" % (threadName, time.ctime(time.time()))
        counter -= 1


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

print "Exiting main Thread"
