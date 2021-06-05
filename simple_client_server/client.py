import socket
s = socket.socket()

port = 12345
s.connect(('127.0.0.1', port))

print('Connected to the server...')
message = s.recv(1024).decode()
print(message)

s.close()
