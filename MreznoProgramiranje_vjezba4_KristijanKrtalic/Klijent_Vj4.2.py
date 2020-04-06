import socket 
from datetime import date


host = socket.gethostname()
port = 5006
client_socket = socket.socket()

client_socket.connect((host, port))
data = client_socket.recv(1024) 
client_socket.sendall(data)

print (data)
client_socket.close()
print (datetime.datetime.now())
