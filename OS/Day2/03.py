# 프로세스 조회
import psutil

psutil.process_iter()

for proc in psutil.process_iter():
    ps_name = proc.name()

    # print(ps_name)  # 돌아가는 프로세스 전체 조회
    if "chrome" in ps_name:
        print(ps_name, proc.pid)