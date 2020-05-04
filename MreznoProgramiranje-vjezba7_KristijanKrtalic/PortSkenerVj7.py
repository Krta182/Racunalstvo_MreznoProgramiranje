import datetime
import socket
import sys
import multiprocessing
import os


def scanPort(arg):
    targetIP,portNum=arg
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result=tcp_sock.connect_ex((targetIP,portNum))
    if result == 0:
        return portNum,True
    else:
        return portNum,False
    sock.close()


def pool_handler(ports):
    cpu_number=multiprocessing.cpu_count()
    print ("Broj jezgri u ovom racunalu je %d jezgri , a koristit cemo %d procesa"% (cpu_number,cpu_number*2))
    pool=multiprocessing.Pool(processes=cpu_number*2)
    
    for port, status in pool.map(scanPort, [(targetIP,port) for port in ports]):
        print ("Skeniram port: %d" % (port)) 
        if status == True:
            print ("port %d je otvoren" %(port)) 
        else: 
            print ("port %d je zatvoren " %(port))
    


def execute():
    global  target, targetIP

    print("Vrijeme pokretanja ovog programa:")
    t1 = datetime.datetime.now()
    print(t1)
    print("----------------------------------------------")

    print("Molim vas unesite adresu hosta koju zelite testirati:")
    target = input(">> ")
    targetIP = socket.gethostbyname(target)

    print("Unesite od kojeg do kojeg porta zelite napraviti skeniranje?")
    start = input("Unesite Pocetni port >> ")
    end = input("Unesite Zavrsni port >> ")
    ports=range(int(start),int(end)+1)
    pool_handler(ports)
  

    t2 = datetime.datetime.now()
    total = t2 - t1
    print("Skeniranje gotovo u: %s" % (total))

# Start Programa
if __name__ == '__main__':

    print("----------------------------------------")
    execute()