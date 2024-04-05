from multiprocessing import Value
import threading

def counter1(snum, cnt):
    try:
        for i in range(cnt):
            snum.value += 1
    finally:
        print('done.')

def counter2(snum, cnt):
    try:
        for i in range(cnt):
            snum.value -= 1
    finally:
        print('done.')

if __name__ == '__main__':
    
    shared_number = Value('i', 0)
    t1 = threading.Thread(target=counter1, args=(shared_number, 10000))
    t1.start()
    
    t2 = threading.Thread(target=counter2, args=(shared_number, 10000))
    t2.start()

    t1.join()
    t2.join()
    print('finally, number is', shared_number.value)