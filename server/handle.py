
import logging
import json
from sqlite3 import connect
FORMAT = "%(asctime)s-%(levelname)s:%(message)s and %(thread)d #thread name:%(threadName)s"
logging.basicConfig(filename='test2.log', level=logging.DEBUG, format=FORMAT)

def newconnection(conn): 
    while True:
        for i in conn:
            data = i.recv(1024)
            if data:
                #for testing purpose
                logging.debug(data.decode())
                i.send(data)



