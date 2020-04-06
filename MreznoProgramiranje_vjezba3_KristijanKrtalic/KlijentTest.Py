import socket 

client_socket=socket.socket()

host_name='www.google.com'
ip_addr=socket.gethostbyname(host_name)
port=80

client_socket.connect((ip_addr,port))
print ("Povezivanje je uspjesno na google server Ip adrese: %s , port %s" %(ip_addr,port))

client_socket.close()