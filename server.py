import socket
import config
from threading import Thread
import logging
import json
from database import *

#set up the logger file.
FORMAT = "%(asctime)s-%(levelname)s:%(message)s and %(thread)d #thread name:%(threadName)s"
logging.basicConfig(filename='test2.log', level=logging.DEBUG, format=FORMAT)

# open the channel
address =(config.HOST, config.PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)
print("Server start >>>>>>")


def newconnection(conn, ip): 
    print(type(ip))
    while True:
        msg = conn.recv(1024)
        if msg:
            storedMessage(ip, msg)
            print(f"{ip}: {msg.decode()}")

while True:
    con, add = s.accept()
    t = Thread(target=newconnection, args=(con,add[0]), name="socket")
    t.daemon=True
    t.start()

