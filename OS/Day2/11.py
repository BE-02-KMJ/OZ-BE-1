from multiprocessing import Process
import os, time

def coke():
    while True:
        try:
            print("coke process id: ", os.getpid())
            print("parent process id: ", os.getppid())
        except KeyboardInterrupt:
            break

def cider():
    while True:
        try:
            print("cider process id: ", os.getpid())
            print("parent process id: ", os.getppid())
        except KeyboardInterrupt:
            break

def milk():
    while True:
        try:
            print("milk process id: ", os.getpid())
            print("parent process id: ", os.getppid())
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    print('11.py Process ID : ', os.getpid())
    child1 = Process(target=coke)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=cider)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=milk)
    child3.start()
    time.sleep(0.5)