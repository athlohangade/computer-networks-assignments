from socket import *
import sys

# define the port to which the socket should bind to receive request from
# cliets. Also define the sending buffer size
s = socket(AF_INET,SOCK_DGRAM)
port = 9999
buf = 1024
s.bind(('', port))

# Get the filename and send the same to client
file_name, addr = s.recvfrom(buf)
s.sendto(file_name, addr)

# read the file send the file in chunks of buf bytes
f=open(file_name.strip(),"rb")
data = f.read(buf)

while (data):
    if(s.sendto(data, addr)):
        print("sending ...")
        data = f.read(buf)

# close the socket and file
s.close()
f.close()
