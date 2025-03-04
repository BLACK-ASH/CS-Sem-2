import socket

s = socket.socket()

host = socket.gethostname()
port = 12345

s.bind((host, port))

s.listen(5)
print("Server started")
print("Waiting for connections")

while True:
    c, addr = s.accept()
    print("Connected to : ", addr)

    c.send(bytes("Hi There", "utf-8"))
    c.close()

    break