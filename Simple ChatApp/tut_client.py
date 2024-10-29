import socket
import time
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.connect(("127.0.0.1",1234))
message = server.recv(1024).decode()
time.sleep(5)
server.send("Hello".encode("utf-8"))

if message:
    server.send("Hello".encode("utf-8"))

server.close()