import time

import threading

seconds = 5
time_start = time.perf_counter()

def timer_func():
    print(f"Вызвался через {time.perf_counter() - time_start} сек") # Вызвался через ~ 5 сек


thr = threading.Timer(seconds, timer_func)
thr.start()

# Также мы можем завершить наш поток раньше чем он успеет отработать например так

time.sleep(seconds - 2)
thr.cancel()

print("Завершаю выполнение")
# В принте будет только Завершаю выполнение,
# принта из функции timer_func не будет, тк она не успеет вызваться