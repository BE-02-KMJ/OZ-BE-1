import threading, os, time

def something(word):
    while True:
        print(word)
        time.sleep(1)

if __name__ == '__main__':
    print('기존 프로세스 아이디: ', os.getpid())
    t = threading.Thread(target=something, args=('happy', ))
    t.daemon = True # 기존 프로세스의 메인 기능이 끝나면 같이 끝난다.
    t.start()
    print('메인 스레드에서 반복문 시작')
    while True:
        try:
            print('daily...')
            time.sleep(1)
        except KeyboardInterrupt:
            print('goodbye ~')
            break