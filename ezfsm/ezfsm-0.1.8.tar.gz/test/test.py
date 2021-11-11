from TimingSeriesFunction import *
import time

my_this = DataArea()


def test():
    this.a = 10


def test2():
    my_this.a = 10


this.a = 999
my_this.a = 114.514

a = time.time()
for i in range(921600):
    my_this.a = 10
print("传统赋值耗时: {}s".format(time.time() - a))

a = time.time()
for i in range(921600):
    this.a = 10
print("包装赋值耗时: {}s".format(time.time() - a))

a = time.time()
for i in range(921600):
    test2()
print("传统赋值耗时(函数): {}s".format(time.time() - a))

a = time.time()
for i in range(921600):
    QuickOuterAreaCall(test, mach, inst, my_this)
print("包装赋值耗时(函数)(快速): {}s".format(time.time() - a))
exit()