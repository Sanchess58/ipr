import socket

from constants import IP, PORT

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.send("Привет, сервер!".encode("utf-8"))

data = client_socket.recv(1)
print(f"Сервер ответил: {len(data)}")

client_socket.close()
