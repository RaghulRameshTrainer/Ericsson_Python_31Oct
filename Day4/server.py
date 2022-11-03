import socketwhile True:


s=socket.socket()
print("Socket successfully created")
port=12345

s.bind(('127.0.0.1',port))
print("Socket binded to {}".format(port))

s.listen(5)
print("socket is listening!")

    c,addr=s.accept()
    print("Received the request from :", addr)
    c.send("Thanks for connecting!".encode('utf-32'))
