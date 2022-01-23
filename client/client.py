import socket, time
add =("10.0.0.86", 8080)
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(add)
s.sendall(b'John')
time.sleep(2)
print(s.recv(128).decode())
