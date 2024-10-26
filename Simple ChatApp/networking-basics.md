# Python Socket Programming and Networking Basics Guide

## Table of Contents
1. [Basic Networking Concepts](#basic-networking-concepts)
2. [Socket Programming Fundamentals](#socket-programming-fundamentals)
3. [Data Flow and Communication](#data-flow-and-communication)
4. [Connection Management](#connection-management)
5. [Error Handling](#error-handling)
6. [Practical Examples](#practical-examples)
7. [Learning Path](#learning-path)

## Basic Networking Concepts

### IP Addresses and Ports
```python
# Common IP Addresses
localhost = '127.0.0.1'    # Your own computer
local_network = '192.168.1.1'  # Typical home network
any_interface = '0.0.0.0'  # Listen on all available interfaces

# Common Ports
common_ports = {
    80: 'HTTP',
    443: 'HTTPS',
    22: 'SSH'
}
# For chat apps, use ports > 1024 (like 5000) to avoid conflicts
```

## Socket Programming Fundamentals

### Client-Server Model
```python
# Server: Waits for connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))  # Host and port
server.listen()  # Start listening for connections

# Client: Initiates connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))  # Connect to server
```

## Data Flow and Communication

### Message Handling
```python
# Sending Data
message = "Hello"
client.send(message.encode('utf-8'))

# Receiving Data
data = client.recv(1024)  # 1024 is buffer size
message = data.decode('utf-8')
```

### Basic Server Example
```python
import socket

def basic_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5000))
    server.listen()
    
    print("Waiting for connection...")
    client, address = server.accept()
    print(f"Connected to {address}")
    
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
                # Echo back
                client.send(f"Got your message: {message}".encode('utf-8'))
        except:
            break
            
    client.close()
    server.close()
```

## Connection Management

### TCP/IP Basics
- TCP ensures reliable delivery
- Messages are delivered in order
- Connection-based (like a phone call)

```python
# TCP Socket (used for chat applications)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### Connection Process
```python
# Server side
server.listen()  # Ready to accept connections
client, addr = server.accept()  # Wait for client

# Client side
client.connect((host, port))  # Initiate connection
```

## Error Handling

### Common Issues and Solutions
```python
# Address already in use
try:
    server.bind(('127.0.0.1', 5000))
except OSError:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 5000))

# Connection refused
try:
    client.connect(('127.0.0.1', 5000))
except ConnectionRefusedError:
    print("Server not running")
```

### Port Testing
```python
def is_port_available(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('127.0.0.1', port))
        available = True
    except:
        available = False
    sock.close()
    return available
```

## Practical Examples

### Echo Server Implementation
```python
import socket

def echo_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('127.0.0.1', 5000))
        server.listen()
        client, addr = server.accept()
        with client:
            while True:
                data = client.recv(1024)
                if not data:
                    break
                client.send(data)  # Echo back
```

### Basic Error Handling Framework
```python
try:
    # Try to connect
    client.connect((host, port))
except ConnectionRefusedError:
    print("Server not running")
except socket.gaierror:
    print("Host not found")
except TimeoutError:
    print("Connection timed out")
```

## Learning Path

### Week 1: Fundamentals
- Learn about IP addresses and ports
- Create basic server that accepts one connection
- Create basic client that can connect

### Week 2: Communication
- Add message sending/receiving
- Implement basic error handling
- Practice with echo server/client

### Week 3: Advanced Features
- Add support for multiple clients
- Implement basic chat functionality
- Add user names/IDs

## Key Points to Remember
1. Always close sockets when done
2. Handle disconnections gracefully
3. Use try/except for network operations
4. Test with multiple clients
5. Start simple, then add features

## Essential Checklist
- [ ] Understanding of IP addresses and ports
- [ ] Basic client-server communication
- [ ] Message encoding/decoding
- [ ] Error handling implementation
- [ ] Multiple client support
- [ ] Clean connection termination

## Common Issues and Solutions
1. Address already in use
   - Solution: Use SO_REUSEADDR socket option
2. Connection refused
   - Solution: Ensure server is running first
3. Data not receiving
   - Solution: Check buffer sizes and encoding
4. Broken pipe
   - Solution: Handle client disconnections properly

Remember to always test your code with multiple scenarios and implement proper error handling for robust applications.
