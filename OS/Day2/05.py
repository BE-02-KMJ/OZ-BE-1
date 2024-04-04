from multiprocessing import Process
import os

def func():
    print('안녕, 나는 실험용 함수야!')
    print('My Process ID : ', os.getpid())
    print('My Parent Process ID : ', os.getppid())

if __name__ == '__main__':
    print('05.py Process ID : ', os.getpid())
    child = Process(target=func).start()