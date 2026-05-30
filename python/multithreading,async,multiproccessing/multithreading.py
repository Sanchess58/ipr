import time
import threading

threads = []


def multithreading_function():
    for i in range(5):
        print(f"Поток {threading.current_thread().name} запустил итерацию {i}")
        time.sleep(1)

if __name__ == "__main__":
    time_start = time.perf_counter()
    for i in range(5):
        thread = threading.Thread(target=multithreading_function, name=f"Thread-{i}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    # В данном случае print в multithreading_function начиная со 2 итерации будет выдавать каждый раз рандомное название 
    # текущего потока, тк тот поток который быстрее получит доступ к этому методу будет его первым обрабатывать

    print(f"Конец обработки задачи в многопоточном режиме. Время: {time.perf_counter() - time_start}") # Время выполнения ~ 5 сек

    # Выполняем ту же задачу, но в 1 потоке
    time_start = time.time()
    for i in range(5):
        multithreading_function()

    print(f"Конец обработки задачи в 1 потоке. Время: {time.time() - time_start}") # Время выполнения ~ 25 сек

# Если требуется чтобы поток завершил свое выполнение вместе с основным потоком,
# то можно передать значение daemon=True
# (в том случае если мы не ждем выполнения всех потоков как в текущей реализации при помощи метода join)

# Пример вывода с daemon=True и без него


def multithreading_function_test_daemon():
    for i in range(5):
        print(f"Поток {threading.current_thread().name} запустил итерацию {i}")
        time.sleep(1)

thread = threading.Thread(target=multithreading_function_test_daemon, name="Thread")
thread.start()

print("Программа завершена")
# В данном случае будет выведено +- такое
# Поток Thread запустил итерацию 0
# Программа завершена
# Поток Thread запустил итерацию 1
# Поток Thread запустил итерацию 2
# Поток Thread запустил итерацию 3
# Поток Thread запустил итерацию 4

# Если же добавить параметр daemon=True -> threading.Thread(target=multithreading_function_test_daemon, name="Thread", daemon=True)
# то вывод будет +- таким
# Поток Thread запустил итерацию 0
# Программа завершена
# тк пока поток спит из-за time.sleep основной поток успевает вывести свой принт и завершить работу
