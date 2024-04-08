import tracemalloc  # python v.3.4 ~ 지원되는 모듈

tracemalloc.start()

# 메모리 할당
data = [b'%d' % num for num in range(1, 10001)] # 1부터 10,000까지 숫자를 문자열로 뿌리기
joined_data = b' '.join(data)   # 리스트 멤버들 사이 공백 추가하고 하나의 문자열로 합쳐진다.

current, peak = tracemalloc.get_traced_memory() # 현재 사용량, 최대 사용량
print(f'현재 메모리 사용량 : {current / 10 ** 6} MB')    # MB로 단위 변경
print(f'최대 메모리 사용량 : {peak / 10 ** 6} MB')

tracemalloc.stop()

# tracemalloc 메모리 사용 기록 조회
traced = tracemalloc.get_tracemalloc_memory()
print(traced / 10 **6)