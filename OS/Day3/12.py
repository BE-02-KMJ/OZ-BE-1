# 파이프 기반의 프로세스 통신
from multiprocessing import Process, Pipe
import os

def send(conn):
    print(f'{os.getpid()}가 {os.getppid()}에게 데이터를 보낸다.')
    conn.send('Hello Parent!')
    conn.close()

if __name__ == '__main__':
    parent, child = Pipe()  # Pipe : 튜플 형태로 두 개의 객체 반환
    p = Process(target=send, args=(child,))
    p.start()
    print('기존 프로세스 아이디: ', os.getpid())
    print(parent.recv())
    p.join()    # 프로세스가 작업을 종료할 때까지 기다린다.
    