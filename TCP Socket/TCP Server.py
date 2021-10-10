import socket #import socket library

print("Welcome to chatting application at server side")

#create socket
s = socket.socket()

#get ip address family or hostname & assign port no.
host = socket.gethostname() 
port = 12221

#assign port no. to socket using
s.bind((host, port))

#allow connection to handle the port using
s.listen(5)

#accept client request
c, addr = s.accept()
print ("Got connection from ", addr)

#in loop accept data from client
while True:
    data = c.recv(1024)
    print("Server received: ", data.decode())

    #accept input from server program user to send to client
    q = input("Server input: ")
    
    if q == "exit":
        q = "Server left chat application"
        c.send(q.encode())
        break

    #send data to client program
    c.send(q.encode())