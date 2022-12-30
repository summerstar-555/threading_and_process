"""
import threading
import time


def hi():
    while 1:
        print("hi")
        time.sleep(1)


def hello():
    while 1:
        print('hello')
        time.sleep(1)
"""
# 使用多线程
"""
hi_thread = threading.Thread(target=hi)     # 这里还有一个小细节：target = hi而不是hi(),也就是说这里如果是函数的话要去掉括号
hello_thread = threading.Thread(target=hello)
hi_thread.start()
hello_thread.start()
"""

# 普通效果
"""
hi()
hello()
"""


# 由于CPython无法做到线程并发，所以后续将使用多进程而非多线程
