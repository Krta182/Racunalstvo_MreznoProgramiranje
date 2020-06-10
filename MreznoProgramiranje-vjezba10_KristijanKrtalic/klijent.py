import socket, datetime
import sys

print ("Vrijeme pokretanja programa : ")

t1 =datetime.datetime.now()

print (t1)
host = socket.gethostname()
port=8000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
print("Unesite svoje ime i prezime")
message=input()

def Main():

    while True: 
        s.send(message.encode('ascii'))
        data=s.recv(1024)
    
        print('Received from the server: ' , str(data.decode('ascii')))
    
        ans=input('Napisite exit da izadete iz programa:  ')
        if ans =='exit':
            print("Bye")
            break
        else:
            continue
        s.close()

if message =='Kristijan Krtalic':
    Main()
else:
    print("Wrong input")
    sys.exit()