import socket

from constants import IP, MAX_BUFFER_SIZE, MAX_CONNECTION, PORT


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(MAX_CONNECTION)
print("Сервер запущен, ожидает подключений")

conn, address = server_socket.accept()
print(f"Подключение установлено с {address}")

data = conn.recv(MAX_BUFFER_SIZE)

conn.send(b"b")

conn.close()
server_socket.close()
