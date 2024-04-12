import concurrent.futures, time

def task(name):
    time.sleep(0.5)
    return f'{name}의 작업이 완료되었습니다.'

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        future_name = { executor.submit(task, f"Task-{i}") : f"Task-{i}" for i in range(5) }
        # print(future_name)

        # 작업이 완료된 순서대로 결과 출력 - 먼저 작업한다고 먼저 끝나진 않는다.
        for future in concurrent.futures.as_completed(future_name):
            name = future_name[future]
            try:
                result = future.result()
                print(f'{name}의 결과 : {result}')
            except Exception as e:
                print(e)