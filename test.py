import asyncio


async def my_coroutine(delay, name):
    await asyncio.sleep(delay)
    return name


async def main():
    coroutines = [
        my_coroutine(3, "Task 1"),
        my_coroutine(1, "Task 2"),
        my_coroutine(2, "Task 3")
    ]

    tasks = [asyncio.create_task(coro) for coro in coroutines]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for future in done:
        result = await future
        print(result)

asyncio.run(main())
