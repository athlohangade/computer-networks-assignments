import socket
import sys

# server ip, server port, and DGRAM indicates udp
HOST = '127.0.0.1'
PORT = 50010
buf = 1024

# make a 3-way handshake and establish TCP connection between server and client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# get the filename
filename = sys.argv[1]

# drop the data to be sent in the TCP connection
s.send(filename.encode())
f = open(filename,'wb')

# receive the data
data = s.recv(buf)
try :
    while data :
        f.write(data)
        print("received packet")
        data = s.recv(buf)

# close the socket and file
except :
    f.close()
    s.close()
    print("File Downloaded")
