import datetime
import socket
import threading


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()

q = queue.Queue()
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for item in source():
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()

 
threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4","Thread-5"]
 

print ("Vrijeme pokretanja ovog programa:")
print (datetime.datetime.now())
print ("Program se izvodi na ovom racunalu:")


print ("---------------------------------------------------------")
print ("Molim vas unesite adresu hosta koju zelite testirati:")
target =input(">> ")
targetIP = socket.gethostbyname(target)
print ("Skeniram host %s, IP adresu: %s" % (target, targetIP))

print ("Unesite od kojeg do kojeg porta zelite napraviti skeniranje?")
start =input("Pocetni port >> ")
end =input("Zavrsni port >> ")


