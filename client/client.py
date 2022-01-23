import socket, time
import config
add = (config.HOST, config.PORT)
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(add)
s.sendall(b'John')
time.sleep(2)
print(s.recv(128).decode())
