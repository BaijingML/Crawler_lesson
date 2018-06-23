import threading
import time

balance = 0
lock = threading.Lock() # 进程锁

def change_it(n):
    global balance
    balance = balance+n
    balance = balance-n

def run_thread(n):
    for i in range(10000):
        lock.acquire()     # 先获得锁，再运行
        try:
            change_it(n)
        finally:
            lock.release()



t1 = threading.Thread(target=run_thread, args = (5, ))
t2 = threading.Thread(target=run_thread, args = (8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)