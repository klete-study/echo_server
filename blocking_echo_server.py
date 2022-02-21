import socket
from _thread import *

client_sockets = []
count = 0
addr = ("127.0.0.1", 9999)

print("server is started ...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(addr)
server_socket.listen()

def threaded(client_socket, addr, count):
    print("client = {}, port = {} ".format(addr[0],addr[1]))
    print("Client{} 접속".format(count))
    while True:
        try:
            data = client_socket.recv(1024)
            if data == None:
                continue

            print('>> Received from {} : {}'.format(addr[1], data.decode()))
            for client in client_sockets:
                client.send(data)
        except:
            pass

try:
    while True:
        client_socket, addr = server_socket.accept()
        count += 1
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr, count,))

except:
    pass
