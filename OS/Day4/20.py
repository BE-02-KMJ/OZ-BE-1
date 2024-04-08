import psutil, os

print("메모리 사용량 조회")

memory_dict = dict(psutil.virtual_memory()._asdict())
# Virtual memory : 시스템 메모리 사용량에 대한 통계를 튜플형식으로 반환
# _asdict : dict 형식으로 변환
print(memory_dict)

total = memory_dict['total']
available = memory_dict['available']
percent = memory_dict['percent']

print(f'메모리 총량 : {total}')
print(f'메모리 즉시 제공 가능량 : {available}')
print(f'메모리 사용률 : {percent}')

pid = os.getpid()
current_process = psutil.Process(pid)

# 현재 나의 프로세스가 얼만큼 메모리를 사용하는지 출력
kb = current_process.memory_info()[0] / 2 ** 20  # KB로 단위 변경
# memory info가 반환하는 이터레이션 데이터의 첫번째 인덱스는 프로세스가 사용한 물리적 메모리의 양
print(f'메모리 사용량 : {kb:.2f} KB')