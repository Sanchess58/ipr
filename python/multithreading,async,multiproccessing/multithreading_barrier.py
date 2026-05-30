import time
import random
import threading


def test_barrier(barrier):
    sleep = random.randint(5, 15)
    time.sleep(sleep)
    print(f"Поток {threading.current_thread().name} тут. Ждал {sleep} сек")

    barrier.wait()
    print(f"Поток {threading.current_thread().name} преодолел барьер")


barrier = threading.Barrier(5)

for i in range(5):
    threading.Thread(target=test_barrier, args=(barrier,)).start()

# Барьер работает таким образом,
# что он блокирует каждый из N-1 количества потоков(это количество передается в класс Barrier) методом .wait
# и после того как N поток вызывает .wait то все эти потоки разблокируются и выполняют дальнейшую логику

# Примерный вывод:
# Поток Thread-3 (test_barrier) тут. Ждал 6 сек
# Поток Thread-2 (test_barrier) тут. Ждал 14 сек
# Поток Thread-4 (test_barrier) тут. Ждал 14 сек
# Поток Thread-5 (test_barrier) тут. Ждал 14 сек
# Поток Thread-1 (test_barrier) тут. Ждал 14 сек
# Поток Thread-1 (test_barrier) преодолел барьер
# Поток Thread-4 (test_barrier) преодолел барьер
# Поток Thread-3 (test_barrier) преодолел барьер
# Поток Thread-5 (test_barrier) преодолел барьер
# Поток Thread-2 (test_barrier) преодолел барьер
