import socket

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1235))



while True:
    full_msg = ""
    new_msg = True
    
    while True:
        # Accept Message
        msg = s.recv(16)
        print(msg)

        if new_msg:
            # Provides the header
            print(f"New message length: {msg[:HEADER_SIZE]}")
            msglen = int(msg[:HEADER_SIZE])
            new_msg = False

        msg = msg.decode("utf-8")
        full_msg += msg

        if len(full_msg)-HEADER_SIZE == msglen:
            print("Full msg recvd")
            print(full_msg[HEADER_SIZE:])
            new_msg = True
            full_msg = ""

        print(full_msg)