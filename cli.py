
# Echo client program
import socket

HOST = 'localhost'
PORT    =  50008# The same port as used by the server  
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world'.encode())  
data = s.recv(1024)  
s.close()
print('Received', repr(data))
