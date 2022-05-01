import socket
import config
from threading import Thread
import time


add = (config.HOST, config.PORT)
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(add)

while True:
    data = input("You message:")
    s.send(data.encode('utf-8'))

    



