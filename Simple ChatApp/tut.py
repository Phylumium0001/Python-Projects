import socket
# # Connecting to google
# try:
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("Socket successfully created")
# except socket.error as err:
#     print("Sockect Creation failed because of ${err}")

# try:
#     host_ip = socket.gethostbyname('www.google.com')
#     print("Host name resolved")
# except socket.gaierror:
#     print("Host name not resolved")

# port = 80

# try:
#     server.connect((host_ip, port))
#     print(f"Socket successfully connected to port {port}")
# except socket.error as err:
#     print("Connection failed because of ${err}")



# Simple Server-Client program

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Reserving a port on my machine
port = 12345

# Binding the socket to the port
# Passing an empty string means that the server can listen to incoming 
# connections from other computers as well.If we would have passed 127.0.0.1 
# then it would have listened to only those calls made within the local computer
try:
    server.bind(('',port))
    print("Binding Complete")
except socket.error as err:
    print("Binding failed because of ${err}")

server.listen(5)
print("Socket is listening")

while True:
    client, address = server.accept()
    print(f"Connection from {address} has been established")
    client.send(bytes("Welcome to the server","utf-8"))
    server.close()
    break