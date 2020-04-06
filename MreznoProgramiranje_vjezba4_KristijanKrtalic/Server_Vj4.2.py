import socket

host = socket.gethostname()
port = 5006

echo_server = socket.socket()
echo_server.bind((host,port))
echo_server.listen(5)

print ("Waiting for client...")
conn, addr = echo_server.accept()
print ("client is connected: ", addr)

while True:
	data = conn.recv(1024)
	if not data: break
	conn.sendall(data)
conn.close()