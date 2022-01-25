import socket
import config
from threading import Thread
import time

def clientthread(f):
    d = f.recv(1024)
    if data:
        print(data)


add = (config.HOST, config.PORT)
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(add)


while True:
    t = Thread(target=clientthread, args=(s,), daemon=True)
    t.start()
    #give ample time for the thread to be execute.
    #for testing. fix it later.
    time.sleep(1)
    data = input("You message:")
    s.send(data.encode('utf-8'))

    



