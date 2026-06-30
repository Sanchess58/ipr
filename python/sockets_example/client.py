import socket
import sys

from constants import IP, MAX_BUFFER_SIZE, PORT

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.send("Привет, сервер!".encode("utf-8"))

data = client_socket.recv(MAX_BUFFER_SIZE)
print(f"Сервер ответил: {sys.getsizeof(data)}")

client_socket.close()
