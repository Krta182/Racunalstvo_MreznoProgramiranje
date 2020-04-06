import socket 

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


server_socket.sendto((UDP_IP,UDP_PORT))

print ("Waiting for connection...")
server_socket.listen(5)

while True:
	conn,addr=server_socket.accept()
	print ('Got connection from',addr)
	conn.send('Server saying hi')
	conn.close()