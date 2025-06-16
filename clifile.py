import socket
s = socket.socket()
host = socket.gethostname()
port = 6000
s.connect((host, port))
with open('received.txt', 'w') as f:
    print('Downloading file..')
    while True:
        data = s.recv(1024)  
        if not data:
            break
        f.write(data.decode())
    print('Received: {}\n'
              .format(data.decode()))
    print('File downloaded successfully.')
s.close()	# Close the socket when done
print('Connection closed')
