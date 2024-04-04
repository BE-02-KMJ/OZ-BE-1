# 내 파이썬 프로그램의 이름
import psutil, os

ps_name = os.getpid()
for proc in psutil.process_iter() :
    if proc.pid == ps_name:
        print(proc.name())