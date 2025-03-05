import socket
s = socket.socket()
s.bind(("localhost",3000))
s.listen(3)
while True:
    c.add = s.accept()
    print("Server Listening On Port",add)
    c.send("Hello World!")
    c.close()
    
