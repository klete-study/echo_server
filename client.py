import socket
from _thread import *

addr = ("127.0.0.1", 9999)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)

        print("recive from server :",data.decode())

start_new_thread(recv_data, (client_socket,))

while True:
    str1 = input('')
    client_socket.send(str1.encode())
