import socket

PORT = 50010
buf = 1024

# create a socket (tcp) and bind to the port and listen to it. maximum 5 queued
# connection requests are allowed
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Allows reusing the same port number
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',PORT))
s.listen(5)

# accept the request and create a new socket called connection socket
conn, addr = s.accept()
print('Connected by' , addr)

while 1 :
        # get the requested filename
        data = conn.recv(1024)
        data = data.decode()
        if not data: 
            break
        print('Received File Request',  repr(data))

        # open the file for readbinary mode, read the file and send the file in
        # chunks of buf bytes
        f=open(data,"rb")
        data = f.read(buf)
        while (data) :
            if(conn.send(data)) :
                print("sending")
                data = f.read(buf)
        break

# close the tcp connection established between the connection port and client port 
conn.close()
s.shutdown(socket.SHUT_RDWR)
s.close()
