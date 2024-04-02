import time

from fastapi import APIRouter

router = APIRouter()


@router.get("/slow-sync-ping")
def slow_sync_ping():
    time.sleep(10)

    return {"msg": "pong"}


import asyncio


@router.get("/slow-async-ping")
async def slow_async_ping():
    await asyncio.sleep(10)

    return {"msg": "pong"}


# 피보나치 수열
def cpu_intensive_task():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    result = fibonacci(35)
    return result


# worst case
# Event Loop 부하 걸림.
async def cpu_hard_task():
    result = await cpu_intensive_task()
    return {"msg": result}


from concurrent.futures import ProcessPoolExecutor


def cpu_bound_task():
    with ProcessPoolExecutor() as executor:
        result = asyncio.get_event_loop().run_in_executor(executor, cpu_intensive_task)  # context switching

    return {"result": result}
