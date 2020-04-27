import datetime
import socket
from queue import Queue
import threading


def scanPort(port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target =input(">>")
    targetIP = socket.gethostbyname(target)
    with print_lock:
        print ("Skeniram host %s, IP adresu: %s" % (target, targetIP))
        print("Skeniram port: %s" %(port)
        # sock = socket.socket()
        result = sock.connect_ex((targetIP, port))
        if result == 0:
            print ("Port %s otvoren" %(port))
        else:
            print ("port je zatvoren %s" %(port))
                sock.close()
    
    except KeyboardInterrupt:
        print ("Pritisili ste Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ("Hostname je nepoznat.Izlazim iz programa...")
        sys.exit()

    except socket.error:
        print ("Nemogu se spojiti na server")
        sys.exit()    
        
def worker():
    while True:
        worker = q.get()
        scanPort(worker)
        q.task_done()    
        
def execute():        

    print ("Unesite od kojeg do kojeg porta zelite napraviti skeniranje?")
    start =input("Unesite Pocetni port >> ")
    end =input(" Unesite Zavrsni port >> ")

      
    print ("Unesite broj niti:")
    num_worker_threads=int(input(">>"))

    q = Queue()
    threads = []
    
    for i in range(num_worker_threads):
            t = threading.Thread(target=worker)
            t.start()
            threads.append(t)


    for worker in range(int(start),int(end)):
            q.put(worker)
            q.join()


    for i in range(num_worker_threads):
            q.put(None)
        for t in threads:
            t.join()
        


    t2 = datetime.datetime.now()

    total =  t2 - t1

    print ("Skeniranje gotovo u: %s" %(total))







#Start Programa

print ("Vrijeme pokretanja ovog programa:")
t1=datetime.datetime.now()
print (t1)

print ("----------------------------------------")
print ("Molim vas unesite adresu hosta koju zelite testirati:")

execute()





