import threading

storage = threading.local()

def get_storage_thread1():
    storage.value = "Value from storage 1"
    print(storage.value)


def get_storage_thread2():
    storage.data = {"value": "Value from storage 2"}
    print(storage.data)

threading.Thread(target=get_storage_thread1).start()
threading.Thread(target=get_storage_thread2).start()
# Value from storage 1
# {'value': 'Value from storage 2'}
# Получить доступ к storage другого потока нельзя,
# упадет ошибка AttributeError: '_thread._local' object has no attribute 'значение атрибута' ниже пример

def get_storage_thread3():
    print(storage.data)

threading.Thread(target=get_storage_thread3).start()
