import socket
s = socket.socket()
print("Socket successfully created")

# Allows reusing the same port number
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 12345
s.bind(('', port))
print("Socket binded to %s" %(port)) 

s.listen(5)
print("Socket is listening")

while 1 :

    conn, addr = s.accept()
    print('Got connection from', addr)

    conn.send('Hello World!!!'.encode())

    conn.close()
