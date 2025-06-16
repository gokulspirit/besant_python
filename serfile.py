import socket

host = socket.gethostname()
port = 6000
s = socket.socket()
s.bind((host, port))
s.listen(5)

print('Server listening..')
while True:
    conn, addr = s.accept()
    print('New Connection from {}'
          .format(addr))  
    with open('test.txt', 'r') as f:
        while True:
            l = f.read(1024) 
            if not l:
                break
            conn.send(l.encode())  
            print('Sent {}'.format(l))
        print('Finished Sending.')
        conn.close()  
print('Connection closed')
