# from multiprocessing import Process, Semaphore, Lock, Queue
# import time
#
# buffer = Queue(10)
# empty = Semaphore(2)
# full = Semaphore(0)
# lock = Lock()
#
# class Consumer(Process):
#     def run(self):
#         global buffer, empty, full, lock
#         while True:
#             full.acquire()
#             lock.acquire()
#             buffer.get()
#             print('Consumer pop an element')
#             time.sleep(1)
#             lock.release()
#             empty.release()
#
# class Producer(Process):
#     def run(self):
#         global buffer, empty, full, lock
#         while True:
#             empty.acquire()
#             lock.acquire()
#             buffer.put(1)
#             print('Producer append an element')
#             time.sleep(1)
#             lock.release()
#             full.release()
#
# if __name__ == '__main__':
#     p = Producer()
#     c = Consumer()
#     p.daemon = c.daemon = True
#     p.start()
#     c.start()
#     p.join()
#     c.join()
#     print('Main Process Ended')
# 那个消费者信号量问题貌似是因为global在不同的进程中只能读，不能写，子进程获得的是一个新的拷贝。把buffer等改成参数传进去就可以解决了
from multiprocessing import Process, Semaphore, Lock, Queue
import time



class Consumer(Process):
    def __init__(self, buffer, empty, full, lock):
        Process.__init__(self)
        self.buffer = buffer
        self.empty = empty
        self.full = full
        self.lock = lock
    def run(self):
        while True:
            self.full.acquire()
            self.lock.acquire()
            self.buffer.get()
            print('Consumer pop an element')
            time.sleep(1)
            self.lock.release()
            self.empty.release()

class Producer(Process):
    def __init__(self, buffer, empty, full, lock):
        Process.__init__(self)
        self.buffer = buffer
        self.empty = empty
        self.full = full
        self.lock = lock
    def run(self):
        while True:
            self.empty.acquire()
            self.lock.acquire()
            self.buffer.put(1)
            print('Producer append an element')
            time.sleep(1)
            self.lock.release()
            self.full.release()

if __name__ == '__main__':
    lock = Lock()
    buffer = Queue(10)
    empty = Semaphore(2)
    full = Semaphore(0)
    p = Producer(buffer, empty, full, lock)
    c = Consumer(buffer, empty, full, lock)
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')
