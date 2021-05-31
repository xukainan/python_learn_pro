import threading
import time


def target1(second):
    print(f'Threading {threading.current_thread().name} is running')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended')


print(f'Threading {threading.current_thread().name} is running')
for i in (1,5):
    thread = threading.Thread(target=target1, args=[i])
    thread.start()
print(f'Threading {threading.current_thread().name} is ended')
