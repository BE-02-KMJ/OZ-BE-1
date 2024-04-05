from multiprocessing import Process
import os, time

def writer():
    print(f'{os.getpid()}가 파일에 쓴다.')
    with open('13.txt', 'w') as f:
        f.write("Hello~")

def reader():
    print(f'{os.getpid()}가 파일을 읽는다.')
    with open('13.txt', 'r') as f:
        print(f.read())

if __name__ == '__main__':
    p1 = Process(target=writer)
    p1.start()

    time.sleep(2)   # Delay를 줌으로서 함부로 쓰는 중에 접근할 수 없게 함.

    p2 = Process(target=reader)
    p2.start()

    p1.join()
    p2.join()