import socket

c = socket.socket()
c.connect(('localhost',8080))
print(c.recv(1024).decode())