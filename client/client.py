import socket
import config
from threading import Thread


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
    data = input("You message:")
    s.send(data.encode('utf-8'))

    



