import time
import asyncio

# В данном примере я показываю две асинхронные задачи, которые выполняются конкурентно с помощью asyncio.sleep() и отрабатывают за 10 секунд.
# И также показываю пример некорректного использования асинхронности, вроде бы написали асинхронные функции, но толку от этого нет, 
# так как внутри них используется time.sleep(), являющийся синхронным методом, который блокирует выполнение и в итоге задачи выполняются последовательно, а не конкурентно.


async def task_async():
    print("Задача 1: начало работы...")
    await asyncio.sleep(10) # имитация долгой работы
    print("Задача 1: работа завершена!")
    return "Результат 1"


async def task_async2():
    print("Задача 2: начало работы...")
    await asyncio.sleep(10) # имитация долгой работы
    print("Задача 2: работа завершена!")
    return "Результат 2"


async def main():
    start_time = time.time()
    task1 = asyncio.create_task(task_async())
    task2 = asyncio.create_task(task_async2())

    await asyncio.gather(task1, task2)
    # Результат принтов:
    # Задача 1: начало работы...
    # Задача 2: начало работы...
    # Задача 1: работа завершена!
    # Задача 2: работа завершена!

    end_time = time.time()
    print(f"Общее время выполнения: {end_time - start_time:.2f} секунд")
    # Общее время выполнения: 10.00 секунд

asyncio.run(main())


async def task():
    print("Задача 1: начало работы...")
    time.sleep(10) # имитация долгой работы
    print("Задача 1: работа завершена!")
    return "Результат 1"


async def task2():
    print("Задача 2: начало работы...")
    time.sleep(10) # имитация долгой работы
    print("Задача 2: работа завершена!")
    return "Результат 2"


async def main_sync():
    start_time = time.time()
    task1_sync = asyncio.create_task(task())
    task2_sync = asyncio.create_task(task2())

    await asyncio.gather(task1_sync, task2_sync)

    # Результат принтов:
    # Задача 1: начало работы...
    # Задача 1: работа завершена!
    # Задача 2: начало работы...
    # Задача 2: работа завершена!

    end_time = time.time()
    print(f"Общее время выполнения: {end_time - start_time:.2f} секунд")
    # Общее время выполнения: 20.01 секунд

asyncio.run(main_sync())
