from socket import *
import sys

# server ip, server port, and DGRAM indicates udp
serverhost = "127.0.0.1"
port = 9999
s = socket(AF_INET, SOCK_DGRAM)

# make a tuple of socket address
# define the buffer size, ie. receive in chunks of 'buf' bytes
addr = (serverhost, port)
buf = 1024

# get the requested filename and send it to server
file_name = sys.argv[1]
s.sendto(file_name.encode(), addr)

# the server sends the filename if file is present on server side, client opens
# the file in writebinary mode
data, addr = s.recvfrom(buf)
print("Received File:", data.decode())
f = open(data.decode(),'wb')

# get the first chunk of data
data, addr = s.recvfrom(buf)

# receive the chunks one by one of size buf and define a timeout period
try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data, addr = s.recvfrom(buf)

# close the file and socket
except timeout:
    f.close()
    s.close()
    print("File Downloaded")
