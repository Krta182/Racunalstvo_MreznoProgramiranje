import datetime
import socket


print ("Vrijeme pokretanja ovog programa:")
t1=datetime.datetime.now()
print (t1)



print ("----------------------------------------")
print ("Molim vas unesite adresu hosta koju zelite testirati:")
target =input(">> ")
targetIP = socket.gethostbyname(target)
print ("Skeniram host %s, IP adresu: %s" % (target, targetIP))
print ("Unesite od kojeg do kojeg porta zelite napraviti skeniranje?")
start =input("Unesite Pocetni port >> ")
end =input(" Unesite Zavrsni port >> ")

print ("Skeniranje unesenog hosta: %s, IP adrese: %s" % (target, targetIP))

try:
    for port in range(int(start),int(end)+1):  
        sock = socket.socket()
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


t2 = datetime.datetime.now()

total =  t2 - t1

print ("Skeniranje gotovo u: %s" %(total))
