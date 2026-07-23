from threading import Thread
import threading
import os
import time


def worker(name):
    print(f"Thread {name}")
    print(f"Thread ID: {threading.get_ident()}")
    print(f"Process ID: {os.getpid()}")
    print("-" * 30)
    time.sleep(2)


t1 = Thread(target=worker, args=("A",))
t2 = Thread(target=worker, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads finished.")
