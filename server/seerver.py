import socket

address =("10.0.0.86", 8080)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(2)

while True:
    con, add = s.accept()
    print("Connected by ", add)
    con.send(b'Hi there!!!')
    data = con.recv(1024).decode()
    
    if data:
        print("Good morning {}".format(data))
