import socket

def simple_server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("127.0.0.1",1234))
    print("Server Created")
    server.listen(5)
    print("Waiting for connection...")
    client, address = server.accept()
    print(f"Connected to {address}")
    
    while True:
        try:
            # Recieving message
            message = client.recv(1024).decode("utf-8")
            if message:
                # Sendin back messages
                client.send(f"Got your message: {message}".encode("utf-8"))
        except:
            break
    client.close()
    server.close()

if __name__ == "__main__":
    simple_server()
