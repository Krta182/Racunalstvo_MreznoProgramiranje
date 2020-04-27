import datetime
import socket
import sys
from queue import Queue
import threading


def scanPort(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock = socket.socket()
    print_lock = threading.Lock()
    with print_lock:
        print("Skeniram host {}, IP adresu: {}".format(target, targetIP))
        print("Skeniram port: {}".format(port))
        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((targetIP, port))
        if result == 0:
            print("Port {} otvoren".format(port))
        else:
            print("port {} je zatvoren ".format(port))
        sock.close()


def threader():
    while True:
        worker = q.get()
        scanPort(worker)
        q.task_done()


def execute():
    global q, target, targetIP

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

    print("Unesite broj niti:")
    num_worker_threads = int(input(">> "))

    q = Queue()

    for i in range(num_worker_threads):
        t = threading.Thread(target = threader)
        t.daemon =True
        t.start()

    for worker in range(int(start), int(end) + 1):
        q.put(worker)

    q.join()

    t2 = datetime.datetime.now()
    total = t2 - t1
    print("Skeniranje gotovo u: %s" % (total))

# Start Programa
if __name__ == '__main__':

    print("----------------------------------------")
    execute()