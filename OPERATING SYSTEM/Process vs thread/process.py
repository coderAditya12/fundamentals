from multiprocessing import Process
import os
import time


def worker(name):
    print(f"Process {name}")
    print(f"PID: {os.getpid()}")
    print(f"Parent PID: {os.getppid()}")
    print("-" * 30)
    time.sleep(2)


if __name__ == "__main__":
    p1 = Process(target=worker, args=("A",))
    p2 = Process(target=worker, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes finished.")
