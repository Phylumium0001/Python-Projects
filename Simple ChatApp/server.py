import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(),1235))
server.listen(5)

HEADER_SIZE = 10

while True:
    clientsocket, address = server.accept()
    print(f'Connection from {address} has been established')

    msg = "Welcome to this amazing server"
    # Header
    msg = f"{len(msg):<{HEADER_SIZE}}" + msg

    clientsocket.send(bytes(msg,"utf-8"))
    timestamp = time.time()
    while True:
        elapsed_time = time.time() - timestamp
        msg = f"Connected for {round(elapsed_time)} seconds\n"
        clientsocket.send(bytes(msg,"utf-8"))
        time.sleep(1)