import socket

s = socket.socket()
print('socket created')
s.bind(('localhost',8080))
s.listen(3)
print('waiting for connections')

while True: 
	c, addr = s.accept()
	print("connected with",addr)
	c.send(bytes("welcomejnsakna","utf-8"))
	c.close()
