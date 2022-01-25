import socket
import config
import handle
from threading import Thread

address =(config.HOST, config.PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)
print("Server start >>>>>>")
clients =[]
while True:
    con, add = s.accept()
    if con in clients:
        pass
    else:
        clients.append(con)
    t = Thread(target=handle.newconnection, args=(clients,), name="socket")
    t.daemon=True
    t.start()

