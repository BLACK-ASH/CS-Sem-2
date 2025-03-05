import socket
s = socket.socket()
host = socket.gethostname()
port = 4000
s.connect((host,port))
print(s.recv(3000))
s.close
