import time
import threading

value = 0

# Пример без блокировок
def inc_value():
    while True:
        global value
        value += 1
        time.sleep(0.5)
        print(value)

for _ in range(3):
    threading.Thread(target=inc_value).start()

# В таком случае, когда N потоков обращаются к одному объекту в памяти, то происходит условие гонки, допустим
# 1 поток пришел заинкрементил value = 0 и значение стало 1,
# грубо говоря "в это же время" пришел 2 поток и тк данные о результате выполнения потока еще не изменились в памяти,
# то 2 поток также думает что value = 0 => 2 подряд принта будут == 1
# В таких случаях нужно использовать блокировки(Lock, RLock) отличие в том, что RLock не дает доступ к разблокировке другим потокам

# Пример с блокировкой Lock

locker = threading.Lock()

def inc_value():
    while True:
        locker.acquire()
        global value
        value += 1
        time.sleep(0.5)
        print(value)
        locker.release()

for _ in range(3):
    threading.Thread(target=inc_value).start()

# В данном примере поток блокирует доступ к выполнению данной логики для других потоков, пока не вызовется .release()
# Если не вызвать release, то следующий поток уже не выполнит логику и программа встанет, как в примере ниже

def inc_value():
    while True:
        locker.acquire()
        global value
        value += 1
        time.sleep(0.5)
        print(value)

for _ in range(3):
    threading.Thread(target=inc_value).start()


# Также можно использовать RLock, чтобы не давать возможности освобождать доступ потоку который не вызывал его блокировку
# В примере ниже 1 поток зайдет в программу и будет в ней работать бесконечно тк RLock не запрещает вызывать блокировку на один и тот же поток несколько раз

locker = threading.RLock()

def inc_value():
    while True:
        locker.acquire()
        global value
        value += 1
        time.sleep(0.5)
        print(value)


for _ in range(3):
    threading.Thread(target=inc_value).start()
