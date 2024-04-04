from multiprocessing import Process
import os, time

def coke():
    print("coke process id: ", os.getpid())
    print("parent process id: ", os.getppid())

def cider():
    print("cider process id: ", os.getpid())
    print("parent process id: ", os.getppid())

def milk():
    print("milk process id: ", os.getpid())
    print("parent process id: ", os.getppid())

if __name__ == '__main__':
    print('07.py Process ID : ', os.getpid())
    child1 = Process(target=coke)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=cider)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=milk)
    child3.start()
    time.sleep(0.5)