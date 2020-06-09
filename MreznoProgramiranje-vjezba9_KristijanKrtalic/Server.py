import socket
import datetime
import ssl

print("Vrijeme pokretanja programa:")
print(datetime.datetime.now())

print("------------------------------------------------")
	
server_socket = socket.socket()
host = "localhost"
port = 8000
	
server_socket.bind((host, port))
print("Waiting for connection...")
server_socket.listen(5)
	
while True:
    conn, addr = server_socket.accept()
    connection_stream = ssl.wrap_socket(conn, server_side=True, certfile="cert.pem", keyfile="key.pem")
    print('Got Connection from ', addr)
    connection_stream.send('Server Saying Hello'.encode())
    connection_stream.shutdown(socket.SHUT_RDWR)
    connection_stream.close()