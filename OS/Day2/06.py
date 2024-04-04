from multiprocessing import Process
import os, time

def func():
    print('안녕, 나는 실험용 함수야!')
    print('My Process ID : ', os.getpid())
    print('My Parent Process ID : ', os.getppid())

if __name__ == '__main__':
    print('06.py Process ID : ', os.getpid())
    child1 = Process(target=func)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=func)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=func)
    child3.start()
    time.sleep(0.5)