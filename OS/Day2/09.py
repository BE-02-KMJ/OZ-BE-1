import threading, os

def func():
    print('안녕, 나는 실험용 함수야!')
    print('My Process ID : ', os.getpid())
    print('Thread ID : ', threading.get_native_id())

if __name__ == '__main__':
    print('This Process ID : ', os.getpid())
    thread1 = threading.Thread(target=func)
    thread1.start()