import socket

#HOST = '192.168.1.56'
HOST = 'localhost'
PORT    =  50008# Arbitrary non-privileged port  
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()  
print('Connected by', addr)  
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data)
    conn.send('Welcome to python'.encode())
conn.close()
