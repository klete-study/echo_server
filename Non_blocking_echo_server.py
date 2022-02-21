# import socket
# import select

# addr = ("127.0.0.1", 9999)
# s = socket.socket()
# s.bind(addr)
# s.listen()
# poll = select.poll()
# poll.register(s, select.POLLIN)
# print("server is started ...")
# input_list = [s]
# while True:
#     input_ready, write_ready, except_ready = select.select(input_list, [], [])
#     for ir in input_ready:
#         if ir == s:
#             client, addr = s.accept()
#             print("client = {} : {} ".format(addr[0],addr[1]))
#             input_list.append(client)
#         else:
#             conn = ir
#             data = conn.recv(1024)
#             if data:
#                 print('>> Received : {}'.format(data.decode()))    
#                 for user in input_list:
#                     if s != user:
#                         user.send(data)

import socket
import select

addr = ("127.0.0.1", 9999)
server = socket.socket()

server.bind(addr)
server.listen()

poller = select.poll()
poller.register(server,select.READ_ONLY)

print("server is started ...")
input_list = [server]

while True:
    input_ready, write_ready, except_ready = select.select(input_list, [], [])
    for ir in input_ready:
        if ir == server:
            client, addr = server.accept()
            print("client = {} : {} ".format(addr[0],addr[1]))
            input_list.append(client)
        else:
            conn = ir
            data = conn.recv(1024)
            if data:
                print('>> Received : {}'.format(data.decode()))    
                for user in input_list:
                    if server != user:
                        user.send(data)
