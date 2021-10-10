import socket #import socket library

print("Welcome to chatting application at client side")

#create socket
s = socket.socket()

#get ip address family or hostname & assign port no.
host = socket.gethostname() 
port = 12221

#establish connect using
s.connect((host, port))

print("Connection established!")

while True:
    z = input("Client input: ")

    if z == "exit":
        break


    #send data to server program using
    s.send(z.encode())

    #receive data from server program using
    data = s.recv(1024)
    print("Client received: ", data.decode())

s.close()