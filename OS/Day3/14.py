from multiprocessing import Process, Value  # Value : 프로세스 간에 값을 공유하게 할 수 있는 생성자 함수

def counter1(snum, cnt):    # snum = shear number
    for i in range(cnt):
        snum.value += 1

def counter2(snum, cnt):
    for i in range(cnt):
        snum.value -= 1

if __name__ == '__main__':
    shared_number = Value('i', 0)   # 0으로 시작하는 int 값 생성
    p1 = Process(target=counter1, args=(shared_number, 5000))
    p1.start()
    
    p2 = Process(target=counter2, args=(shared_number, 5000))
    p2.start()

    p1.join()
    p2.join()
    print('finally, number is', shared_number.value)